import os
import pandas as pd
from complements import helper as h
from complements import analyses as a
from complements  import plotting as p


def accuracy (dataset_names, plotname = '_accuracy_plot'):

    """This Function calculats accuray from raw data for one or
    multiple given datasets. Accuracy is computed for all human
    observers and models across all difficulty levels. Per dataset
    the function outputs two plots (average classification
    accuracy and normalised classification accuracy) and a csv
    file with the raw accuracies (find those in the folders figures &
    raw_accuracy). """

    PLOT_PATH = h.get_plot_path()

    for dataset in dataset_names:

        print(dataset)

        # preparation and data loading
        acc_summary = pd.DataFrame(columns=['observer', 'difficulty', 'accuracy'])
        observers = ['4_6', '7_9', '10_12', '13_15', 'adults', 'vgg19', 'resnext', 'bitm', 'swsl', 'swag'] 
        diff_level = h.get_diff_levels(dataset)
        dfs = h.get_data_as_dfs(dataset)

        # get mean accuracy for each age group and model across different difficulty levels
        countdfs = 0
        for df in dfs:
            df["difficulty"] = df['difficulty'].astype(str)
            for level in diff_level:
                dfLevel = df
                for i, row in dfLevel.iterrows():
                    if row['difficulty'] != level:
                        dfLevel = dfLevel.drop(i)
                result = a.sixteen_class_accuracy(dfLevel)
                dict = {'observer': observers[countdfs], 'difficulty': level, 'accuracy': result.get("16-class-accuracy")}
                acc_summary = acc_summary.append(dict, ignore_index = True)
            countdfs += 1

        # print and save results
        print(acc_summary)
        acc_summary.to_csv(("/home/rebushulk/Documents/GitHub/JoV/data_analysis/raw_accuracy/" + dataset + ".csv"), index=False)
        
        #prepare data for plotting
        data4_6 = (acc_summary.loc[acc_summary['observer'] == '4_6'])['accuracy'].tolist()
        data7_9 = (acc_summary.loc[acc_summary['observer'] == '7_9'])['accuracy'].tolist()
        data10_12 = (acc_summary.loc[acc_summary['observer'] == '10_12'])['accuracy'].tolist()
        data13_15 = (acc_summary.loc[acc_summary['observer'] == '13_15'])['accuracy'].tolist()
        dataadults = (acc_summary.loc[acc_summary['observer'] == 'adults'])['accuracy'].tolist()
        dataDnn1 = (acc_summary.loc[acc_summary['observer'] == 'vgg19'])['accuracy'].tolist()
        dataDnn2 = (acc_summary.loc[acc_summary['observer'] == 'resnext'])['accuracy'].tolist()
        dataDnn3 = (acc_summary.loc[acc_summary['observer'] == 'bitm'])['accuracy'].tolist()
        dataDnn4 = (acc_summary.loc[acc_summary['observer'] == 'swsl'])['accuracy'].tolist()
        dataDnn5 = (acc_summary.loc[acc_summary['observer'] == 'swag'])['accuracy'].tolist()

        # plotting
        if dataset== "noise":
            
            p.accuracy_plot(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname),
                            data4_6,data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5,
                             xlabel="Noise level",
                            axis=[-0.01,0.38,0,1.05],
                            yLocator = 0.1, xLocator = 0.05, positionsData = [0,.1,.2,.35], positionsChance = [0,.35],
                            plot_legend = False)

            p.accuracy_plot_normalised(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname + "_normalised"),
                            data4_6,data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5, 
                            xlabel="Noise level", axis=[-0.01,0.38,0,1.05],
                            yLocator = 0.1, xLocator = 0.05, positionsData = [0,.1,.2,.35])

        elif dataset == "eidolon":
            p.accuracy_plot(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname),
                            data4_6,data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5,
                             xlabel="Log\u2082 of 'reach' parameter", axis=[-.1,4.5,0,1.05],
                            yLocator = 0.1, xLocator = 1, positionsData = [0,2,3,4], positionsChance = [0,4],
                            plot_legend=True)

            p.accuracy_plot_normalised(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname + "_normalised"),
                            data4_6,data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5,
                            xlabel="Log\u2082 of 'reach' parameter", axis=[-.1,4.5,0,1.05],
                            yLocator = 0.1, xLocator = 1, positionsData = [0,2,3,4])

        elif dataset == "cue_conflict":

            # Note. The following accuracy plots are not in the paper. In these plots only correct shape desicions are correct
            # responses. Compare to Shape-bias figures in the paper where correct texture as well as correct shape decisions 
            # are correct reponses.

            p.accuracy_plot(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname),
                            data4_6,data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5,
                            xlabel= "Image type", axis=[-0.08,1.1,0,1.05],
                            yLocator = 0.1, xLocator = 1, positionsData = [0,1], positionsChance = [0,1],
                            plot_legend = False)

            p.accuracy_plot_normalised(dataset, (PLOT_PATH + 'accuracy/' + dataset + plotname + "_normalised"),
                            data4_6, data7_9, data10_12, data13_15, dataadults, dataDnn1, dataDnn2, dataDnn3, dataDnn4, dataDnn5,
                            xlabel= "Image type", axis=[-0.08,1.1,0,1.05],
                            yLocator = 0.1, xLocator = 1, positionsData = [0,1])

if __name__ == "__main__":

    datasets = ['noise', 'eidolon', 'cue_conflict']
    accuracy(datasets)