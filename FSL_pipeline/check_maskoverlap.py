# christinadelta
# date: 15/07/2017

# This follows the level 1 checking script

import os
import glob

# We will start with the registration png files
outfile = "/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/lev2_QA.html"
os.system("rm %s"%(outfile))

all_feats = glob.glob('//Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/sub*/model/lev2.gfeat/')

f = open(outfile, "w")
for file in list(all_feats):
  f.write("<p>============================================")
  f.write("<p>%s"%(file))
  f.write("<IMG SRC=\"%s/inputreg/masksum_overlay.png\">"%(file))
  f.write("<IMG SRC=\"%s/inputreg/maskunique_overlay.png\">"%(file))
f.close()
