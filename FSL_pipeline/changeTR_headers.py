# christinadelta
# date: 10/07/2017

import glob
import os
import sys
import subprocess
import commands

path = '/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/'
bold_files = glob.glob('%s/sub[0-9][0-9][0-9]/BOLD/task001_run00[1-9]/bold.nii.gz'%(path))

for cur_bold in list(bold_files):
    print(cur_bold)
    # strip off .nii.gz from file name (makes code below easier)
    out = commands.getstatusoutput('fslinfo %s | grep "pixdim"'%(cur_bold))
    out_split = str.split(out[1])
    pixdim1 = out_split[1]
    pixdim2 = out_split[3]
    pixdim3 = out_split[5]
    pixdim4 = 2  # TR goes here, change if TR is different than 2.
    os.system('fslchpixdim %s %s %s %s %s'%(cur_bold, pixdim1, pixdim2, pixdim3, pixdim4))
