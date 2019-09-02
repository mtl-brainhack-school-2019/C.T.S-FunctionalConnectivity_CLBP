##### Remove the warnings to keep notebook cleaner #####
import warnings
warnings.filterwarnings('ignore')


##### Fetching Brain Parcellations #####
#Fetching Schaefer 400-Parcellations
from nilearn import datasets
work_dir = '/Volumes/Harddrive_CTS/MRI/Placebo_1_Analysis/'
schaefer_parcellations = datasets.fetch_atlas_schaefer_2018(n_rois = 400, yeo_networks = 7, data_dir = work_dir)
labels_schaefer = schaefer_parcellations.labels 
atlas_schaefer = schaefer_parcellations.maps
print('Schaefer Atlas ROIs are located in nifti image (4D) at: %s' %
       atlas_schaefer)
#Fetching Yeo 7-Network
yeo_parcellations = datasets.fetch_atlas_yeo_2011(data_dir = work_dir, verbose = 1)
atlas_yeo = yeo_parcellations.thin_7
print('Yeo Atlas ROIs are located in nifti image (4D) at: %s' %
       atlas_yeo)
#Fetching Power 264-parcellations
power = nilearn.datasets.fetch_coords_power_2011()
print('Power atlas comes with {0}.'.format(power.keys()))
#Compute spheres of fixed radius of sequence (x,y,z)
import numpy as np
power_coords = np.vstack((power.rois['x'], power.rois['y'], power.rois['z'])).T
print('Stacked power coordinates in array of shape {0}.'.format(power_coords.shape))


#Plot Atlases
%matplotlib gtk
import matplotlib.pyplot as plt
from nilearn import plotting
# Schaefer
plotting.plot_roi(atlas_schaefer, title='Schaefer 400-Parcellations Atlas',
                  cut_coords=(8, -4, 9), colorbar=True, cmap='Paired')
plt.show()
# Yeo
plotting.plot_roi(atlas_yeo, title='Yeo 7-Network (thin) Atlas',
                  cut_coords=(8, -4, 9), colorbar=True, cmap='Paired')
plt.show()


##### Connectivity Measures #####
from nilearn.connectome import ConnectivityMeasure
C_measure = ConnectivityMeasure(kind = 'correlation')
PC_measure = ConnectivityMeasure(kind = 'partial correlation')

##### Create Nifti Label Mask #####
#Atlases
from nilearn.input_data import NiftiLabelsMasker
sch_masker = NiftiLabelsMasker(labels_img = atlas_schaefer, standardize = True, memory = 'nilearn_cache', verbose = 1)
yeo_masker = NiftiLabelsMasker(labels_img = atlas_yeo, standardize = True, memory = 'nilearn_cache', verbose = 1)
#Spheres
from nilearn import input_data
pow_masker = input_data.NiftiSpheresMasker (
    seeds = power_coords, smoothing_fwhm = 4, radius = 5.,
    detrend = True, standardize = True, low_pass = 0.1, high_pass = 0.01, t_r = 2.5)

#from glob import glob
#import os
#DataDir = '/lustre03/project/6037352/tangsab8/CLBP_Network_Project/FMRIPREP_OUTPUT/fmriprep/sub-*/ses-2/func/'
#print(DataDir)
# Bold Nifti File of interest
#Data = sorted(glob(os.path.join(DataDir, '*_ses-2_task-rest_run-1_space-MNI152NLin6Asym_desc-preproc_bold.nii.gz')))
# Confound .tsv file of interest
#Confounds = sorted(glob(os.path.join(DataDir, '*regressors.tsv')))
#print(Confounds)
#print(Data)
#len(Data)

##### Loading Nifti Data #####
import pandas as pd
import numpy as np
#Defining Data Directory
data_dir = '/Volumes/Harddrive_CTS/MRI/Placebo_1_Analysis/FMRIPREP_OUTPUT/'
#Task label & Space name
task_label = 'rest'
space_name = 'MNI152NLin6Asym'
#List of subjects
list_subjects = ['sub-001',
'sub-003',
'sub-005']
N=len(list_subjects)
#Models for Nifti image
print_sub_S2R1 = []
models_path_imgs_S2R1 = []
models_path_confs_S2R1 = []
all_time_series_yeo_S2R1 = []
all_time_series_sch_S2R1 = []
all_time_series_pow_S2R1 = []
list_C_matrix_yeo = []
list_C_matrix_sch = []
list_PC_matrix_yeo = []
list_PC_matrix_sch = []
#Loop for path & confounds
for sub in list_subjects:
      #Create paths
      path_img_S2R1 = data_dir + sub + '/' + sub + '_ses-2' + '_task-' + task_label + '_run-1' + '_space-' + space_name + '_desc-preproc_bold.nii.gz'
      path_conf_S2R1 = data_dir + sub + '/' + sub + '_ses-2' + '_task-' + task_label + '_run-1' + '_desc-confounds_regressors.csv'
      #Append paths to a list
      models_path_imgs_S2R1.append(path_img_S2R1)
      models_path_confs_S2R1.append(path_conf_S2R1)
      #Select confounds of choice
      try:
            pd_conf_S2R1 = pd.read_csv(path_conf_S2R1, sep=',')
      except:
            print("File not present")
      else:
            pd_conf_S2R1 = pd.read_csv(path_conf_S2R1, sep=',')
            print_sub_S2R1.append(sub)
            c_S2R1= pd_conf_S2R1[['csf', 'white_matter', 'global_signal', 'trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z']]
            conf_S2R1 = c_S2R1.to_csv(path_conf_S2R1)
      #Create time-series & append to a list
      time_series_yeo_S2R1 = yeo_masker.fit_transform(path_img_S2R1, confounds = conf_S2R1)
      all_time_series_yeo_S2R1.append(time_series_yeo_S2R1)
      time_series_sch_S2R1 = sch_masker.fit_transform(path_img_S2R1, confounds = conf_S2R1)
      all_time_series_sch_S2R1.append(time_series_sch_S2R1)
      time_series_pow_S2R1 = pow_masker.fit_transform(path_img_S2R1, confounds = conf_S2R1)
      all_time_series_pow_S2R1.append(time_series_yeo_S2R1)
      # Creates time-series (AND POWER MATRICE)
      C_matrices_yeo_S2R1 = C_measure.fit_transform(all_time_series_yeo_S2R1)
      print('Correlations of CLBP patients are stacked on yeo atlas in an array of shape {0}'.format(C_matrices_yeo_S2R1))
      C_matrices_sch_S2R1 = C_measure.fit_transform(all_time_series_sch_S2R1)
      print('Correlations of CLBP patients are stacked on schaefer atlas in an array of shape {0}'.format(C_matrices_sch_S2R1))
      PC_matrices_yeo_S2R1 = PC_measure.fit_transform(all_time_series_yeo_S2R1)
      print('Partial Correlations of CLBP patients are stacked on yeo atlas in an array of shape {0}'.format(PC_matrices_yeo_S2R1))
      PC_matrices_sch_S2R1 = PC_measure.fit_transform(all_time_series_sch_S2R1)
      print('Partial Correlations of CLBP patients are stacked on schaefer atlas in an array of shape {0}'.format(PC_matrices_sch_S2R1))
      #Averaging time-series
      mean_C_matrix_yeo_S2R1 = C_matrices_yeo_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_C_matrix_yeo_S2R1))
      mean_C_matrix_sch_S2R1 = C_matrices_sch_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_C_matrix_sch_S2R1))
      mean_PC_matrix_yeo_S2R1 = PC_matrices_yeo_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_PC_matrix_yeo_S2R1))
      mean_PC_matrix_sch_S2R1 = PC_matrices_sch_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_PC_matrix_sch_S2R1))
      # Averaging group time-series
      list_C_matrix_yeo_S2R1.append(mean_C_matrix_yeo_S2R1)
      list_C_matrix_sch_S2R1.append(mean_C_matrix_sch_S2R1)
      list_PC_matrix_yeo_S2R1.append(mean_PC_matrix_yeo_S2R1)
      list_PC_matrix_sch_S2R1.append(mean_PC_matrix_sch_S2R1)
print('Data has {0} subjects.'.format(len(list_subjects))

#Merge list of interest
filename_id = pd.concat([print_sub], [print_ses], [print_run], axis = 1)



      mean_C_matrix_yeo_S2R1 = C_matrices_yeo_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_C_matrix_yeo_S2R1))
      mean_C_matrix_sch_S2R1 = C_matrices_sch_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_C_matrix_sch_S2R1))
      mean_PC_matrix_yeo_S2R1 = PC_matrices_yeo_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_PC_matrix_yeo_S2R1))
      mean_PC_matrix_sch_S2R1 = PC_matrices_sch_S2R1.mean
      print('Mean correlation has shape {0}.'.format(mean_PC_matrix_sch_S2R1))




##### Deriving our own ICA components #####
from nilearn.decomposition import CanICA
canica = CanICA(n_components=7, smoothing_fwhm=5.,
                memory="nilearn_cache", memory_level=2,
                threshold=5., verbose=10, random_state=0)
canica.fit(path_img_S2R1)
#Saving the components as Nifti
components_img = canica.components_img_
components_img.to_filename('/Volumes/Harddrive_CTS/MRI/Placebo_1_Analysis/canica_resting_state.nii.gz')
#Visualize all components on a plot
%matplotlib gtk
from nilearn.plotting import plot_prob_atlas
import matplotlib.pyplot as plt
from nilearn import plotting
plot_prob_atlas(components_img, title='All 7 ICA components')
# Mapping components each ICA seperately
from nilearn.image import iter_img
from nilearn.plotting import plot_stat_map, show
for i, cur_img in enumerate(iter_img(components_img)):
    plot_stat_map(cur_img, display_mode = "z", title = "IC %d" % i,
                  cut_coords = 1, colorbar = False)


#See paths images
models_run_imgs


#See path confounds
models_run_confs




