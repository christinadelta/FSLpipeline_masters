# christinadelta
# date: 04/07/2017

import glob
import os

# first check the data
path = '/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/'
boldfiles = glob.glob('%s/sub0[0-9][0-9]/BOLD/task00[0-9]_run00[0-9]/bold.nii.gz'%(path))

for file in boldfiles:
    print file
    os.system("fslnvols %s"%(file))

# check subdirectories
subdirs = glob.glob('%s/sub[0-9][0-9][0-9]'%(path))

# run BET (brain extraction)
for dir in subdirs:
    print dir
    # Only run the following if your orientation was mixed up
    # BUT directional labels must be accurate in fslview
    # Make sure you verify that it worked
    #os.system("fslreorient2std  %s/anatomy/highres001  %s/anatomy/highres001"%(dir,dir))
    # bet call edit to use the flags you found worked well on your data
    os.system("bet %s/anatomy/highres001 %s/anatomy/highres001_brain -R -m"%(dir,dir))
