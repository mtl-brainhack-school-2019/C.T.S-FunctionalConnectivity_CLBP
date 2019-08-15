#### Functional Connectivity on Chronic Low Back Pain (CLBP) patients ####
## By Christophe Tanguay-Sabourin (GitHub: CTanguay-Sabourin)##

Here is my project for the Brain Hack School 2019. 

## Which dataset do I want to analyze? ##
For my project, I will use a dataset available on **OpenPain**, an open access data sharing platform for brain imaging studies of human pain. You can find the data set *Placebo_1* on http://www.openpain.org/index.html, provided by the Apkarian Lab, situated in Northwestern University.

*NOTE: The structural data are currently not available on OpenPain (only functional data), but they should be in September.*

![CLBP](http://dev.www.health.harvard.edu/media/content/images/L0714e-1.jpg)

This dataset comes from an RCT study investigating the determinants of placebo response. I will use the control group (i.e without placebo treatment; 68 participants) using their structural (T1w) and functioncal (rsfMRI) scans, during their first scanning sessions. For more information about the dataset, you may also refers to its original study:

#### Vachon-Presseau, E., Berger, S. E., Abdullah, T. B., Huang, L., Cecchi, G. A., Griffith, J. W., … Apkarian, A. V. (2018). Brain and psychological determinants of placebo pill response in chronic pain patients. *Nature communications*, 9(1), 3397. #####

## Which tools do I want to learn? ##

* **Fmiprep**, as my pre-processing pipeline.

* **Compute Canada (Beluga)**, as my computing platform

* **Python**, as my programming language

* **Jupyter**, as my notebook for codes, visualizations and narratives.

* **Nilearn**, for my neuroimaging analysis and brain parcellations.

![Schaeffer](https://pbs.twimg.com/media/Dz2u7WCU8AIxNJ4.jpg)


* **Netneurotools**, for some of my functional connectivity analysis (tools from *Bratislav Mišić*), using PLS and *bootstrap ratios* as a cross-validation method.

## Which kind of deliverable do I want to implement: analysis, code, data, tutorial...? ##

- [x] Scripts to install and operate (*sbatch*) fmriprep on Compute Canada

- [

- [ ] Jupyter Notebook with complete analysis

## What kind of medium will I use to present my results? ##



### What I'm aiming to do in this project: ###
* Install and operate fmriprep pre-processing on Compute Canada clusters
* Write all my scripts (from the installation of fmriprep on Beluga to my statistical analysis) in python & bash 
    * They will all be posted on GitHub repo
* Make a Jupyter Notebook of my analysis
* Export different brain parcellations (types & sizes) to implement in the functional connectivity
      * Network Modules (17 parcellations, by Yeo 2011 and ???)
      * Fine-grain parcellations (400 parcellations, by Schaefer & Yeo 2018 and 264 parcellations, by Power & Peterson 2011)
* Write and run a script for functional connectivity analysis
* Cross-validate my results







