
import pandas as pd

from complements import helper as h
from complements import analyses as a
from complements import plotting as p

PLOT_PATH = h.get_plot_path()

def shape_bias(dataset):

    # get all data from the cue_conflict experiment into one df
    dfs = h.get_data_as_dfs(dataset)
    df = pd.concat(dfs)
    df = df.reset_index(drop=True)

    # get df containing only cue_conflict images
    for i, row in df.iterrows():
        imagename = str(row['imagename'])
        if imagename.split("_")[3] != "1":
            df = df.drop(i)            
    df = df.reset_index(drop=True)

    # analysis and plotting
    p.plot_shapebias(PLOT_PATH + "shapeB/shape_bias",df, order_by='humans')
    p.plot_shape_bias_boxplot(PLOT_PATH + "shapeB/box_plot_shape_bias",df)

if __name__ == "__main__":

    dataset = 'cue_conflict'
    shape_bias(dataset)