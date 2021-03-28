# christinadelta
# date: 12/07/2017

# This alternative is creating the html file on one machine, but viewing on another.
# For example, you use a remote Linux system and viewing the html is too slow and it won't fully load for printing

import os
import glob

# We will start with the registration png files
outfile = "/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/QA_example2/lev1_QA.html"
outdir = "/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/QA_example2/"

os.chdir(outdir)

os.system("rm %s"%(outfile))
os.system("rm -rf files")
os.system("mkdir files")

all_feats = glob.glob('/Users/christinadelta/Datasets/OpenNeuro/FSL_preproDatasets/fatcat_project/sub*/model/task001_run00*.feat/')

f = open(outfile, "w")
for file in list(all_feats):
  f.write("<p>============================================")
  f.write("<p>%s"%(file))
  f.write("<IMG SRC=\"files/%s.design.png\">"%(file.replace("/", "_")))
  f.write("<IMG SRC=\"files/%s.design_cov.png\" >"%(file.replace("/", "_")))
  f.write("<IMG SRC=\"files/%s.disp.png\">"%(file.replace("/", "_")))
  f.write("<IMG SRC=\"files/%s.trans.png\" >"%(file.replace("/","_")))
  f.write("<p><IMG SRC=\"files/%s.example_func2highres.png\" WIDTH=1200>"%(file.replace("/","_")))
  f.write("<p><IMG SRC=\"files/%s.example_func2standard.png\" WIDTH=1200>"%(file.replace("/","_")))
  f.write("<p><IMG SRC=\"files/%s.highres2standard.png\" WIDTH=1200>"%(file.replace("/","_")))
  os.system("cp %s/design.png files/%s.design.png"%(file, file.replace("/","_")))
  os.system("cp %s/design_cov.png files/%s.design_cov.png"%(file, file.replace("/","_")))
  os.system("cp %s/mc/disp.png files/%s.disp.png"%(file, file.replace("/","_")))
  os.system("cp %s/mc/trans.png files/%s.trans.png"%(file, file.replace("/", "_")))
  os.system("cp %s/reg/example_func2standard.png files/%s.example_func2standard.png"%(file,  file.replace("/","_")))
  os.system("cp %s/reg/example_func2highres.png files/%s.example_func2highres.png"%(file, file.replace("/","_")))
  os.system("cp %s/reg/highres2standard.png files/%s.highres2standard.png"%(file, file.replace("/","_")))
f.close()
