# christinadelta
# date: 10/07/2017

# There is likely a better way to do this! Need to work on this
# Basically, I'm using python to create a text file with a huge command in it and then we run it.

import os
import glob

# We will start with the registration png files
outfile = "/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/QA/lev1_QA.html"
os.system("rm %s"%(outfile))

all_feats = glob.glob('/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/sub*/model/task001_run00*.feat/')

f = open(outfile, "w")
for file in list(all_feats):
  f.write("<p>============================================")
  f.write("<p>%s<br>"%(file))
  f.write("<IMG SRC=\"%s/design.png\">"%(file))
  f.write("<IMG SRC=\"%s/design_cov.png\" >"%(file))
  f.write("<IMG SRC=\"%s/mc/disp.png\">"%(file))
  f.write("<IMG SRC=\"%s/mc/trans.png\" >"%(file))
  f.write("<p><IMG SRC=\"%s/reg/example_func2highres.png\" WIDTH=1200>"%(file))
  f.write("<p><IMG SRC=\"%s/reg/example_func2standard.png\" WIDTH=1200>"%(file))
  f.write("<p><IMG SRC=\"%s/reg/highres2standard.png\" WIDTH=1200>"%(file))
f.close()
