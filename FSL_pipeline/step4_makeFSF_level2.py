# christinadelta
# date: 15/07/2017


# This creates the level2 fsf's and the script to run the feats on condor

import os
import glob

studydir = '/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/'

fsfdir="%s/Scripts/fsfs"%(studydir)


subdirs=glob.glob("%s/sub[0-9][0-9][0-9]"%(studydir))

for dir in list(subdirs):
    splitdir = dir.split('/')
    splitdir_sub = splitdir[5]  # You will need to edit this
    subnum=splitdir_sub[-3:]    # You also may need to edit this
    subfeats=glob.glob("%s/model/task001_run00[0-9].feat"%(dir))
    if len(subfeats)==3:  # Add your own second loop for 2 feat cases
        print(subnum)
        replacements = {'SUBNUM':subnum}
        with open("%s/template_lev2.fsf"%(fsfdir)) as infile:
            with open("%s/lev2/design_sub%s.fsf"%(fsfdir, subnum), 'w') as outfile:
                for line in infile:
                    for src, target in replacements.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)
