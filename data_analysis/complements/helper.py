import os
import pandas as pd

"""
Various helper functions for data analysis
"""


# helper function to move up from a given path
def dir_up(path,n): # here 'path' is your path, 'n' is number of dirs up you want to go
    for _ in range(n):
        path = dir_up(path.rpartition("/")[0], 0) 
    return(path)

# get difficulty level labels for different experiments
def get_diff_levels (dataset_name):

    possible_names = ['noise', 'eidolon', 'cue_conflict']

    assert dataset_name in possible_names, "Faulty dataset name; use 'noise', 'eidolon', or 'cue_conflict'"

    if dataset_name == 'noise':
        diff_level = ["0.0","0.1", "0.2", "0.35"]
    elif dataset_name == 'eidolon':
        diff_level = ["0", "4", "8", "16"]
    elif dataset_name == 'cue_conflict':
        diff_level = ["0","1"]
    return diff_level

def get_observer_labels():
    return ['4-6','7-9','10-12','13-15','adults','vgg19','resnext','bitm','swsl','swag']

# get raw data from psychophysical experiments as dataframe for each age group and model
def get_data_as_dfs(dataset_name):
    CWD = os.getcwd()
    RAW_DATA = dir_up(CWD,1) + '/data/'
    df1 = pd.read_csv(RAW_DATA + dataset_name + '/humans/4_6.csv')
    df2 = pd.read_csv(RAW_DATA + dataset_name + '/humans/7_9.csv')
    df3 = pd.read_csv(RAW_DATA + dataset_name + '/humans/10_12.csv')
    df4 = pd.read_csv(RAW_DATA + dataset_name + '/humans/13_15.csv')
    df5 = pd.read_csv(RAW_DATA + dataset_name + '/humans/adults.csv')
    dfDnn1 = pd.read_csv(RAW_DATA + dataset_name + '/models/vgg19.csv')
    dfDnn2 = pd.read_csv(RAW_DATA + dataset_name + '/models/resnext.csv')
    dfDnn3 = pd.read_csv(RAW_DATA + dataset_name + '/models/bitm.csv')
    dfDnn4 = pd.read_csv(RAW_DATA + dataset_name + '/models/swsl.csv')
    dfDnn5 = pd.read_csv(RAW_DATA + dataset_name + '/models/swag.csv')

    return [df1, df2, df3, df4, df5, dfDnn1, dfDnn2, dfDnn3, dfDnn4, dfDnn5]

def get_plot_path():
    CWD = os.getcwd()
    return dir_up(CWD,1) + '/figures/'

def get_acc (df):
    return len(df.loc[df.object_response == df.category]) / len(df)

def get_category_lables():
    return sorted (["knife", "keyboard", "elephant", "bicycle", "airplane",
            "clock", "oven", "chair", "bear", "boat", "cat",
            "bottle", "truck", "car", "bird", "dog"])

def get_df_for_delta(age_groups):
    """Insert two of the following age groups:
    4_6, 7_9, 10_12, 13_15, or adults. For these 
    age groups this function provides a data frame 
    each, contaning the data regarding performance 
    on distorted images for both experiments 
    (eidolon and noise)."""

    CWD = os.getcwd()
    RAW_DATA = dir_up(CWD,1) + '/data/'
    df_noise_1 = pd.read_csv(RAW_DATA + 'noise/humans/' + age_groups[0] + '.csv')
    df_noise_2 = pd.read_csv(RAW_DATA + 'noise/humans/' + age_groups[1] + '.csv') 
    df_eidolon_1 = pd.read_csv(RAW_DATA + 'eidolon/humans/' + age_groups[0] + '.csv')
    df_eidolon_2 = pd.read_csv(RAW_DATA + 'eidolon/humans/' + age_groups[1] + '.csv') 

    df_age_1 = [df_noise_1, df_eidolon_1]
    df_age_1 = pd.concat(df_age_1)
    df_age_2 = [df_noise_2, df_eidolon_2]
    df_age_2 = pd.concat(df_age_2)

    df_age_1 = df_age_1.loc[df_age_1['difficulty'] < 0.01]
    df_age_2 = df_age_2.loc[df_age_2['difficulty'] < 0.01]

    return [df_age_1, df_age_2]

def get_dataframe_row (df, age_group):
    return df.loc[df.age == age_group, ['minute','8_seconds', 'second', 'fixation']].values.flatten().tolist()
    
def clean_df_for_errorK(df):
    df = df[df['condition'] != '10-12 vs. 10-12']
    df = df[df['condition'] != '13-15 vs. 13-15']
    df = df[df['condition'] != '4-6 vs. 10-12']
    df = df[df['condition'] != '4-6 vs. 13-15']
    df = df[df['condition'] != '7-9 vs. 10-12']
    df = df[df['condition'] != '7-9 vs. 13-15']
    df = df[df['condition'] != '10-12 vs. 13-15']
    df = df[df['condition'] != '10-12 vs. Adults']
    df = df[df['condition'] != '10-12 vs. DNNs']
    df = df[df['condition'] != '13-15 vs. Adults']
    df = df[df['condition'] != '13-15 vs. DNNs']
    return df

def get_data_for_errorK(dataset_name):
    CWD = os.getcwd()
    RAW_DATA = dir_up(CWD,1) + '/data/error_consistency/'
    df1 = pd.read_csv(RAW_DATA + dataset_name + '0' + '.csv')
    df1 = clean_df_for_errorK(df1)
    df2 = pd.read_csv(RAW_DATA + dataset_name + '1' + '.csv')
    df2 = clean_df_for_errorK(df2)
    df3 = pd.read_csv(RAW_DATA + dataset_name + '2' + '.csv')
    df3 = clean_df_for_errorK(df3)
    df4 = pd.read_csv(RAW_DATA + dataset_name + '3' + '.csv')
    df4 = clean_df_for_errorK(df4)

    dfs = [df1, df2, df3, df4]
    
    return dfs


    