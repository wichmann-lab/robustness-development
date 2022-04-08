import pandas as pd
import os

PATH = '/home/rebushulk/Documents/GitHub/JoV/data/cue_conflict/models/'

PATHS = os.listdir(PATH)

PATHS = [PATH + x for x in PATHS]

models = ['vgg19', 'resnext', 'bitm', 'swsl', 'swag']

count = 0

for path in PATHS:
    df = pd.read_csv(path)

    for i, row in df.iterrows():

        diff = row['imagename'].split('_')[3]
        df.iloc[i, 14] = diff


        # if len(row['category'].split('-')) == 2:
        #     new_cat = (row['category'].split('-')[0])[:-1]
        #     new_cat = new_cat.replace("1", "") 
        #     df.iloc[i,5] = new_cat
    
    df.to_csv(path, index=False)
    count+=1
