#### Building Analysis Templates for Functional Connectivity on Chronic Low Back Pain (CLBP) patients for my lab and myself ####
## By Christophe Tanguay-Sabourin (GitHub: CTanguay-Sabourin)##

Here is my project for the Brain Hack School 2019. 

## Purpose of this repository ##
This repository provides the basics (and relevant ressources) on how to use Compute Canada Servers, fMRIprep pre-processing pipeline as well as doing various standard functional connectivity measures on nilearn, explained through a jupyter notebook. 

## My Project ##
My project will be to introduce Compute Canada and fMRIprep to my fellow lab members. This includes the necessary informations et ressources to create an account, connect to the cluster, to know how to use a terminal, to import fMRIprep and run jobs with fMRIprep. 

Additionally, I will also include in a jupyter notebook the necessary basics to run the following analyses & visualization: 
- Present two differents ways to load (slow with structure vs fast without structure)
- Fetching parcellations (Yeo's and Schaefer's; and how to plot them)
- Derive ICA networks from the groups & plot them together/individually
- Extract spheres from specific coordinates
- Apply masks on the nifti files for region-of-interest
- Run time-series, and make correlations/partial correlation/tangent between the ROIs
- Extract summary measures as numpy array for the group or each participant.

This notebook will use the *Placebo_1* Dataset, freely available from **OpenPain** (see: http://www.openpain.org/index.html).

*NOTE: The structural data are currently not available on OpenPain (only functional data), but they will  be in the 10th of September.*

![CLBP](http://dev.www.health.harvard.edu/media/content/images/L0714e-1.jpg)


This dataset comes from an RCT study investigating the determinants of placebo response. I will use the control group (i.e without placebo treatment; 68 participants) using their structural (T1w) and functioncal (rsfMRI) scans, during their first scanning session. For more information about the dataset, you may also refers to its original study:

#### Vachon-Presseau, E., Berger, S. E., Abdullah, T. B., Huang, L., Cecchi, G. A., Griffith, J. W., … Apkarian, A. V.         (2018). Brain and psychological determinants of placebo pill response in chronic pain patients. *Nature communications*,       9(1), 3397. ####

## Which tools do I want to learn? ##

* **Fmiprep**, as my pre-processing pipeline.

![fmriprep](https://pbs.twimg.com/media/Dbt_hXeVQAEZHTS.jpg)

* **Compute Canada (Beluga)**, as my computing platform

![ComputeCanada](https://www.ace-net.ca/wp-content/uploads/2018/03/Compute_Canada2.png)

* **Python**, as my programming language

![Python](https://content.techgig.com/thumb/msid-67886887,width-860,resizemode-4/How-Developers-use-Python-Programming-Language.jpg?50999)

* **Jupyter**, as my notebook for codes, visualizations and narratives.

![JupyterNotebook](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/250px-Jupyter_logo.svg.png)

* **Nilearn**, for my neuroimaging analysis and brain parcellations.

![Nilearn](https://danilobzdok.de/wp-content/uploads/sites/521/ni-learn.jpg)

                  Schaeffer & Yeo, 2018. 400 Brain Parcellations derived within the 7 Network Modules
                  
![Schaeffer](https://pbs.twimg.com/media/Dz2u7WCU8AIxNJ4.jpg)

                  Power & Peterson, 2011. 264 Brain Parcellations; network modules can also be mapped.
                  
![Power](https://ars.els-cdn.com/content/image/1-s2.0-S0896627311007926-gr1.jpg)


* **Netneurotools**, for some of my functional connectivity analysis (tools from *Bratislav Mišić*), using PLS and *bootstrap ratios* as a cross-validation method.

![Netneurotools](https://avatars0.githubusercontent.com/u/31446908?s=400&v=4)



I will be associating the brain connectivity with classics questionnaires in clinical pain, descriptive of the severity:

* **McGill Pain Questionnaire (MPQ)**, assess the quality and intensity of pain.

![MPQ](https://ars.els-cdn.com/content/image/3-s2.0-B9781416058939002227-gr4.jpg)

* **Beck Depression Inventory (BDI)** to measure the severity of depression symptoms

![BDI-II](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjS09OMu4XkAhXPUt8KHSyTA9QQjRx6BAgBEAQ&url=%2Furl%3Fsa%3Di%26source%3Dimages%26cd%3D%26ved%3D%26url%3D%252Furl%253Fsa%253Di%2526source%253Dimages%2526cd%253D%2526ved%253D%2526url%253Dhttps%25253A%25252F%25252Fchicagomindsolutions.com%25252Fcontact%25252Fintake-forms%25252Fbdi%25252F%2526psig%253DAOvVaw0xRtmhHsb5qmBEiMI72RYH%2526ust%253D1565978614036427%26psig%3DAOvVaw0xRtmhHsb5qmBEiMI72RYH%26ust%3D1565978614036427&psig=AOvVaw0xRtmhHsb5qmBEiMI72RYH&ust=1565978614036427)

![](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi9ypHHuoXkAhUrZN8KHeOMAdoQjRx6BAgBEAQ&url=%2Furl%3Fsa%3Di%26source%3Dimages%26cd%3D%26ved%3D%26url%3Dhttps%253A%252F%252Fwww.increase-project.eu%252Fimages%252FDOWNLOADS%252FIO2%252FEN%252FCURR_M2-A12_Beck-Depr-Invent_(EN-only)_20170920_EN_final.pdf%26psig%3DAOvVaw3d3wcJC7iylcjLKMFDVrFh%26ust%3D1565978466357272&psig=AOvVaw3d3wcJC7iylcjLKMFDVrFh&ust=1565978466357272)


* **Ecological Momentary Assessement**, to sample pain daily in real time, in subject's environment for 2 weeks.
    * Mean
    * Peak
    * Standard Deviation

![EMA](https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiYyLXSuYXkAhVSU98KHQftAF4QjRx6BAgBEAQ&url=https%3A%2F%2Filumivu.com%2Fsolutions%2Fecological-momentary-assessment-app%2F&psig=AOvVaw2AyVledoIzTBriL7mW_5rQ&ust=1565978228121062)

## Which kind of deliverable do I want to implement: analysis, code, data, tutorial...? ##

- [x] [ **Code** ] Scripts to install and operate (*sbatch*) fmriprep on Compute Canada

- [ ] [ **Code & Analysis** ] Python script of my functional connectivity & cross-validation analysis

- [ ] [ **Data** ] Present my output data obtained from fmriprep

- [ ] [ **Notebook** ] Make the script on a Jupyter Notebook, with all the relevant explanations of the analysis.

- [ ] [ **Notebook & Analysis** ] Provide some vizualizations of my preliminary results from nilearn and netneurotools

## What kind of medium will I use to present my results? ##

#### A Jupyter Notebook presenting all my preliminary results, visualizations and explanations ####

#### A folder on my repository with a copy of all my scripts used in this project ####








