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

#### What I learn in brainhack #####
I would like to say *everything*. During a single month, I tripled or quadripuled the amount of knowledge I had on computer science-related and neuroimaging knowledge I had.

Not only I had the occasion to learn in a supportive environment how to implement open tools in my own projects, but I also learned what else exist out there. I was thought tools that I might not immediately use on my current thesis, but I now have a familiarity with them, can refers them to some of my collegues or implement them in future projects.

## Which tools did I learned primarily? ##

* **Fmiprep**, as my pre-processing pipeline.
![fmriprep](https://pbs.twimg.com/media/Dbt_hXeVQAEZHTS.jpg)

* **Compute Canada (Beluga)**, as my computing platform
![ComputeCanada](https://www.ace-net.ca/wp-content/uploads/2018/03/Compute_Canada2.png)

* **Globus**, to for rapid file transfer on Compute Canada
![Globus](https://mytechdecisions.com/wp-content/uploads/2019/07/globus_logo_small.png)

* **Python**, as my programming language
![Python](https://content.techgig.com/thumb/msid-67886887,width-860,resizemode-4/How-Developers-use-Python-Programming-Language.jpg?50999)

* **Jupyter Notebook**, as my notebook for codes, visualizations and narratives.
![JupyterNotebook](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/250px-Jupyter_logo.svg.png)

* **Nilearn**, for my neuroimaging analysis.
![Nilearn](https://danilobzdok.de/wp-content/uploads/sites/521/ni-learn.jpg)

* **Numpy is & Panda**, for data management

![Numpy](https://meshlogic.github.io/posts/jupyter/linear-algebra/linear-algebra-numpy-1/numpy-logo.png)
![Pandas](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/03/pandas.jpg)

* **Conda (Computer; localy) or virtualenv (Beluga; remotely)**, to create seperate virtual environment for every projects I run
![Virtualenv](https://miro.medium.com/max/750/1*FjqLQ08MEk6jSKxpzjCcVw.jpeg)

## Which tools will I intend to learn later in my own research career ##
*(Now that I was familarized with them through Brain Hack)*
One of my personal goal in research would be develop a platform from which brain imaging could be used more easily in the clinic. This woull be particularly useful in the long run if it provides insight from objective physiological measurements for the diagnostic or the severity assessments of certain diseases. This is especially true for pain, where **there exist no objective measurements for suffering**.

* **Docker**, as my container to import the processing and analyses tools necessary.

* **Deep Learning**, as a proxy for pre-processing (idea discussed by Pierre)
*Within the context of increasing sample sizes, it would be now possible to develop a deep-learning algorithm that mimic pre-processing. This would result a significant reduction in the pre-processing power as well as a reduction in the size of the files*

* **Machine Learning**, for clinical assessment/diagnostic 
*As shown with various studies, the complexity captured from DL often leads to overfit in clinical design and does not provide increased performance over simpler ML*

## Which kind of deliverable do I want to implement: analysis, code, data, tutorial...? ##

- [x] [ **Code** ] Scripts to install and operate (*sbatch*) fmriprep on Compute Canada

- [x] [ **Code & Analysis** ] Python script of functional connectivity analyses

- [ ] [ **Data** ] Present my output data obtained from fmriprep

- [ ] [ **Notebook** ] Make the script on a Jupyter Notebook, with all the relevant explanations of the analysis.

- [ ] [ **Notebook & Analysis** ] Provide some vizualizations of my preliminary results from nilearn and netneurotools

## What kind of medium will I use to present my results? ##

#### A Jupyter Notebook presenting all my preliminary results, visualizations and explanations ####

#### A folder on my repository with a copy of all my scripts used in this project ####








