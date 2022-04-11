from complements import helper as h
from complements import plotting as p


PLOT_PATH = h.get_plot_path()

def errorK (datasetnames, plot_path):

    # get data
    for dataset in datasetnames:
        dfs = h.get_data_for_errorK(dataset)

        #plotting
        p.errorK_multi_boxplot(dfs, dataset, plot_path + 'errorK/')

if __name__ == "__main__":

    datasets = ['eidolon', 'noise']
    errorK(datasets, PLOT_PATH)

