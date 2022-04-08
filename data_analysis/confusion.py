import math

import helper as h
import analyses as a
import plotting as p

def confusion_matrices(datasets):

    # peparation
    PLOT_PATH = h.get_plot_path()
    observer_labels = h.get_observer_labels()
    categories = h.get_category_lables()

    for dataset in datasets:

        #get data
        dfs = h.get_data_as_dfs(dataset)
        diff_levels = h.get_diff_levels(dataset)

        # confusion analysis and plotting
        countdfs = 0
        for df in dfs:
            df["difficulty"] = df['difficulty'].astype(str)
            lst = []
            for level in diff_levels:
                dfLevel = df

                for i, row in dfLevel.iterrows():
                    if row['difficulty'] != level:
                        dfLevel = dfLevel.drop(i)
                result = a.confusion_matrix(dfLevel, categories)
                result = result.round(2)
                lst.append(result)
            p.plot_confusion_matrix_single(lst, (PLOT_PATH + 'confusionM/' + dataset + '_' + observer_labels[countdfs]))
            countdfs +=1

if __name__ == "__main__":

    datasets = ['noise', 'eidolon', 'cue_conflict']
    confusion_matrices(datasets)