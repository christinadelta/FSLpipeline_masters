# christinadelta
# date: 07/07/2017

import glob
import os
import sys
import subprocess

path = '/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/'

# grab all the bold files
bold_files = glob.glob('%s/sub[0-9][0-9][0-9]/BOLD/task001_run00[1-9]/bold.nii.gz'%(path))

# I'm using a big html file to put all QA info together
outhtml = "/Users/christinadelta/Documents/MRI/output/ds008/bold_motioncor.html"
out_bad_bold_list = "/Users/christinadelta/Documents/MRI/output/ds008/subs_lose_gt_45_vol_scrub.txt"

os.system("rm %s"%(out_bad_bold_list))
os.system("rm %s"%(outhtml))

for cur_bold in list(bold_files):
    print(cur_bold)
    # Store directory name
    cur_dir = os.path.dirname(cur_bold)

    # strip off .nii.gz from file name (makes code below easier)
    cur_bold_no_nii = cur_bold[:-7]

'''
    # I can also use fslreorient2std BUT
    # SHOULD NOT RUN THIS UNLESS DATA ACTUALLY NEED IT! If needs to be run, uncomment below:
    os.system("fslswapdim %s z -x -y %s_swapped"%(cur_bold_no_nii, cur_bold_no_nii))
    # Once we're confident this works correctly, we can change the above to
    # overwrite bold.nii.gz (it saves disc space)

    # This is used to trim off unwanted volumes
    # DO NOT USE THIS UNLESS YOU'VE DOUBLE CHECKED HOW MANY VOLUMES NEED TO BE TRIMMED (IF ANY)
    # This trims first 2 and I set the max to a number far beyond
    # the number of TRs
    # Correct filename here to use output of previous step (if used)
    os.system("fslroi %s %s_trimmed 2 300"%(cur_bold_no_nii, cur_bold_no_nii))
    # Once you're confident this works correctly, you can change the above to
    # overwrite bold.nii.gz '''

    # Assessing motion.  This is what takes the longest
    # Check current literature to see if this thresh (0.9) is
    # acceptable
    # I got it from here: http://www.ncbi.nlm.nih.gov/pubmed/23861343
    # Also, consider using FSL's FIX to clean your data
    if os.path.isdir("%s/motion_assess/"%(cur_dir))==False:
        os.system("mkdir %s/motion_assess"%(cur_dir))
        os.system("fsl_motion_outliers -i %s -o %s/motion_assess/confound.txt --fd --thresh=0.9 -p %s/motion_assess/fd_plot -v > %s/motion_assess/outlier_output.txt"%(cur_bold_no_nii, cur_dir, cur_dir, cur_dir))

    # Put confound info into html file for review later on. First add outlier information, then fd_plot.png
    os.system("cat %s/motion_assess/outlier_output.txt >> %s"%(cur_dir, outhtml))
    os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s/motion_assess/fd_plot.png WIDTH=100%s></BODY></HTML>' >> %s"%(cur_dir, cur_dir,'%', outhtml))

    # If we're planning on modeling out scrubbed volumes later
    # it is helpful to create an empty file if confound.txt isn't
    # generated (i.e. no scrubbing needed).  It is basically a
    # place holder to make future scripting easier
    if os.path.isfile("%s/motion_assess/confound.txt"%(cur_dir))==False:
        os.system("touch %s/motion_assess/confound.txt"%(cur_dir))

    # Very last, create a list of subjects who exceed a threshold for
    # number of scrubbed volumes.  This should be taken seriously.  If
    # most of our scrubbed data are occurring during task, that's
    # important to consider (e.g. subject with 20 volumes scrubbed
    # during task is much worse off than subject with 20 volumes
    # scrubbed during baseline.
    output = subprocess.check_output("grep -o 1 %s/motion_assess/confound.txt | wc -l"%(cur_dir), shell=True)
    num_scrub = [int(s) for s in output.split() if s.isdigit()]

    if num_scrub[0]>45:
        with open(out_bad_bold_list, "a") as myfile:
            myfile.write("%s\n"%(cur_bold))
