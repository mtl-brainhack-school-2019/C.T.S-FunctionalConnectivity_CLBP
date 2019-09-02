#### Building Analysis Templates for Functional Connectivity on Chronic Low Back Pain (CLBP) patients for my lab and myself ####
## By Christophe Tanguay-Sabourin (GitHub: CTanguay-Sabourin)##

Here is my project for the Brain Hack School 2019. 

## Purpose of this repository ##
This repository provides the basics (and relevant ressources) on how to use Compute Canada Servers, fMRIprep pre-processing pipeline as well as doing various standard functional connectivity measures on nilearn, explained through a jupyter notebook. 

## My Project ##
My project will be to introduce Compute Canada and fMRIprep to my fellow lab members. This includes the necessary informations et ressources to create an account, connect to the cluster, to know how to use a terminal, to import fMRIprep and run jobs with fMRIprep. 

Additionally, I will also include in a few **jupyter notebook** presenting the necessary basics to run the following analyses & visualization: 
- Present two differents ways to load (slow with structure vs fast without structure)
- Fetching parcellations (Yeo's and Schaefer's; and how to plot them)
- Derive ICA networks from the groups & plot them together/individually
- Extract spheres from specific coordinates
- Apply masks on the nifti files for region-of-interest
- Run time-series, and make correlations/partial correlation/tangent between the ROIs
- Extract summary measures as numpy array for the group or each participant.

![CLBP_Infographic](https://github.com/mtl-brainhack-school-2019/Christophe_FunctionalConnectivity_CLBP/blob/master/Christophe_CLBP%20Infographic.png?raw=true)
*As explained in this infographic, chronic pain is a worldwide disability. Using brain imaging, we hope to derive objective markers of pain and suffering using the brain*

#### Dataset ####
This notebook will use the *Placebo_1* Dataset, freely available from **OpenPain** (see: http://www.openpain.org/index.html).
*NOTE: The structural data are currently not available on OpenPain (only functional data), but they will  be in the 10th of September.*

#### What you will need #####
- You will need to create an account on Compute Canada. See the following folder ( https://github.com/mtl-brainhack-school-2019/Christophe_FunctionalConnectivity_CLBP/blob/master/1.%20UsefulCodeForBeluga.md ).

## Which tools am I using? ##

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


## Which kind of deliverable do I want to implement: analysis, code, data, tutorial...? ##

- [x] [ **Code** ] Scripts to install and operate (*sbatch*) fmriprep on Compute Canada

- [ ] [ **Code & Analysis** ] Python script of my functional connectivity & cross-validation analysis

- [ ] [ **Data** ] Present my output data obtained from fmriprep

- [ ] [ **Notebook** ] Make the script on a Jupyter Notebook, with all the relevant explanations of the analysis.

- [ ] [ **Notebook & Analysis** ] Provide some vizualizations of my preliminary results from nilearn and netneurotools

## What kind of medium will I use to present my results? ##

#### A Jupyter Notebook presenting all my preliminary results, visualizations and explanations ####

#### A folder on my repository with a copy of all my scripts used in this project ####








