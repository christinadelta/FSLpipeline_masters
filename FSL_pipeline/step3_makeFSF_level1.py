# christinadelta
# date: 10/07/2017

import os
import glob

# Set path of the data to be analysed
path = '/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/'

# Set this to the directory where you'll dump all the fsf files
# May want to make it a separate directory, because you can delete them all
# once Feat runs
fsfdir="%s/Scripts/fsfs"%(path)

# Get all the paths!  Note, this won't do anything special to omit bad subjects
subdirs=glob.glob("%s/sub[0-9][0-9][0-9]/BOLD/task001_run0[0-9][0-9]"%(path))

for dir in list(subdirs):
  splitdir = dir.split('/')
  # YOU WILL NEED TO EDIT THIS TO GRAB sub001
  splitdir_sub = splitdir[8]
  subnum=splitdir_sub[-3:]
  #  YOU WILL ALSO NEED TO EDIT THIS TO GRAB THE PART WITH THE RUNNUM
  splitdir_run = splitdir[10]
  runnum=splitdir_run[-3:]
  print(subnum)
  ntime = os.popen('fslnvols %s/bold.nii.gz'%(dir)).read().rstrip()
  replacements = {'SUBNUM':subnum, 'NTPTS':ntime, 'RUNNUM':runnum}
  with open("%s/template_lev1.fsf"%(fsfdir)) as infile:
      with open("%s/lev1/design_sub%s_run%s.fsf"%(fsfdir, subnum, runnum), 'w') as outfile:
        for line in infile:
          # Note, since the video, I've changed "iteritems" to "items"
          # to make the following work on more versions of python
          #  (python 3 no longer has iteritems())
          for src, target in replacements.items():
              ine = line.replace(src, target)
          outfile.write(line)
