
import pandas as pd

import helper as h
import analyses as a
import plotting as p

PLOT_PATH = h.get_plot_path()

def shape_bias(dataset):

    dfs = h.get_data_as_dfs(dataset)
    df = pd.concat(dfs)
    df = df.reset_index(drop=True)

    for i, row in df.iterrows():
        imagename = str(row['imagename'])

        if imagename.split("_")[3] != "1":
            df = df.drop(i)            
    df = df.reset_index(drop=True)

    df['object_response'] = df['object_response'].str.strip()
    df['category'] = df['category'].str.strip()
            
    for i, row in df.iterrows():
        if len(row['category'].split('-')) >=2:
            new_cat = (row['category'].split('-')[0])[:-1]
            new_cat = new_cat.replace("1", "") 
            df.iloc[i,5] = new_cat

    p.plot_shapebias(PLOT_PATH + "shapeB/shape_bias",df, order_by='humans')
    p.plot_shape_bias_boxplot(PLOT_PATH + "shapeB/box_plot_shape_bias",df)

if __name__ == "__main__":

    dataset = 'cue_conflict'
    shape_bias(dataset)