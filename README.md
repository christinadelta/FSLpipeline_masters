# FSL pipeline for my masters project
The pipeline that I used to analyse my fMRI data for my master's project

This has not been used ever since then (2017)!

Dependencies: FSL, python3 and FreeSurfer (in some cases)

## The steps of the pipeline to run an fMRI analysis using python scripts and FSL:
* Step 1: check all your anatomical and bolds paths etc and run bet (bet extraction)
* Step 2: prepare the functional data
* Step 3: make FSF for level 1 analysis
* check your level 1 outputs
* Step 4: make fsf FOR level 2 analysis (within)
* check your level 2 outputs
* Step 5: runs level 3 (group level) analysis
* check your level 3 outputs

### NOTE:
These scripts run in combination with GUI interaction. For example, I prefer to do a lot of pre-processing stuff (like motion correction, etc.., through the GUI). Also, analysis of level 3 (step 5 is done through the gui entirely). 



