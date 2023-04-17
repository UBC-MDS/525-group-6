# 525-group-6

## Members:

-   HanChen Wang
-   Crystal Geng
-   Tony Zoght
-   Chester Wang

## Quick access to milestone submissions

Milestone 1: <https://github.com/UBC-MDS/525-group-6/blob/main/notebooks/DSCI_525_lab1.ipynb>

Milestone 2: <https://github.com/UBC-MDS/525-group-6/blob/main/milestone2/Milestone2.ipynb>

Milestone 3: <https://github.com/UBC-MDS/525-group-6/blob/main/milestone3/Milestone3.ipynb>

## Introduction

In this project, our objective is to get familiar with processing datasets and constructing machine learning models at scale. We will be working with a dataset containing daily precipitation data from New South Wales (NSW), Australia, covering the years from 1889 to 2014. The dataset is derived from CMIP6, a global cooperative initiative that brings together climate modeling outputs from various research groups.

The dataset comprises 6 columns, which represent timestamps, spatial data, and rainfall amounts (in mm/day). Our initial task (milestone 1) involves consolidating the modelled datasets into a single CSV file to facilitate subsequent processing. As the project progresses, we anticipate developing and deploying ensemble machine learning models in the cloud to forecast daily rainfall in Australia based on the dataset. The dataset features outputs from multiple climate models, with the actual rainfall observation as the target variable.

We have sourced the dataset from [figshare](https://docs.figshare.com/), and our ultimate aim is to develop an ensemble model that leverages these outputs and compare its predictions with the actual rainfall data. By the end of the project, we aim to have a cloud-deployed machine learning model available for public use.

## Description

In milestone 1, we downloaded data from [figshare](https://docs.figshare.com/) and combined multiple datasets into a single CSV file. We then performed exploratory data analysis (EDA) using Python and R. Subsequently, in milestone 2, we established an Amazon EC2 instance with JupyterHub and an S3 bucket. We transferred the data from milestone 1 to our S3 bucket and conducted further data wrangling to prepare for machine learning.

For milestone 3, we developed a `RandomForestRegressor` model and evaluated its performance against other individual climate models by comparing their root mean square error (RMSE). The ensemble model, `RandomForestRegressor`, demonstrated better performance with a lower RMSE, and we proceeded to fine-tune its hyperparameters. To accomplish this, we set up an EMR cluster and utilized a PySpark notebook to perform hyperparameter tuning.

After conducting hyperparameter tuning, we discovered that `n_estimators = 100` and `max_depth = 5` were the best-performing hyperparameters. Using these parameters, we trained our model and achieved a train RMSE of 8.10 and a test RMSE of 7.81. Our tuned model demonstrated reasonable performance, prompting us to save it for deployment in milestone 4.
