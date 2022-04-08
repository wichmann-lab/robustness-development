import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import seaborn as sns
import os
from collections import OrderedDict
from matplotlib.ticker import FormatStrFormatter
import colors as c
import helper as h
import analyses as a

import decision_makers as dm

def accuracy_plot(datasetname, path,
                    dataA, dataB, dataC, dataD, dataE, dataF, dataG, dataH, dataI, dataJ,
                    xlabel,
                    axis, yLocator, xLocator,
                    positionsData, positionsChance, plot_legend = False):
                    
    plt.rcParams['font.size'] = '16'
    # plt.rcParams["font.family"] = "serif"

    fig = plt.figure(figsize=(7,6))
    axes = plt.subplot(1,1,1)
    ax = plt.axes()
    axes.axis(axis)

    axes.xaxis.set_major_locator(MultipleLocator(xLocator))
    axes.yaxis.set_major_locator(MultipleLocator (yLocator))

    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)


    plt.plot(positionsChance, [.0625,.0625], linestyle=":",linewidth=1, color="k", label="Chance performance")
    plt.plot(positionsData, dataA, 'o', linestyle="-", linewidth=1.5, markersize=8, color=c.age1, label="4-6 year-olds")
    plt.plot(positionsData, dataB, 'o', linestyle="-", linewidth=1.5, markersize=8, color=c.age2, label="7-9 year-olds")
    plt.plot(positionsData, dataC, 'o', linestyle="-", linewidth=1.5, markersize=8, color=c.age3,label="10-12 year-olds")
    plt.plot(positionsData, dataD, 'o', linestyle="-", linewidth=1.5, markersize=8, color=c.age4, label="13-15 year-olds")
    plt.plot(positionsData, dataE, 'o', linestyle="-", linewidth=1.5, markersize=8, color=c.age5, label="Adults")
    plt.plot(positionsData, dataF, 's', linestyle="-", linewidth=1.5, markersize=8, color=c.vgg19, label="VGG-19 (>1M)")
    plt.plot(positionsData, dataG, '^', linestyle="-", linewidth=1.5, markersize=9, color=c.resnext, label="ResNeXt (>1M)")
    plt.plot(positionsData, dataH, 'D', linestyle="-", linewidth=1.5, markersize=8, color=c.bitm, label="BiT-M (>10M)")
    plt.plot(positionsData, dataI, 'p', linestyle="-", linewidth=1.5, markersize=9, color=c.swsl, label="SWSL (>100M)")
    plt.plot(positionsData, dataJ, 'h', linestyle="-", linewidth=1.5, markersize=9, color=c.swag, label="SWAG (>1,000M)")


    plt.xlabel(xlabel)
    if datasetname == "cue_conflict":
        plt.xticks([0, 1], ['Original', 'Cue-conflict'])
    elif datasetname == "noise":
        plt.xticks(positionsData, ['0', '0.1', '0.2', '0.35'])
    elif datasetname == "eidolon":
        plt.xticks(positionsData, ['0', '2', '3', '4'])
    

    plt.ylabel("Classification accuracy")
    plt.tight_layout()
    sns.despine(trim=True)

    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    labels = list(by_label.values())[::-1] #reverse label order
    handles = list(by_label.keys())[::-1] #reverse handle order

    if plot_legend == True:
        plt.legend(labels, handles,loc=(0.03,0.08), frameon = False, prop={'size': 12})

    plt.savefig(path, bbox_inches='tight', dpi=150)
    plt.close()

def accuracy_plot_normalised(datasetname, path, dataA, dataB, dataC, dataD, dataE, dataF, dataG, dataH, dataI, dataJ,
                    xlabel, 
                    axis, yLocator, xLocator,
                    positionsData):

    def normalize2(a,b):
        onepercent = a/1
        y = 1
        z = b/onepercent
        return([y,z])

    def normalize(a,b,c,d):
        onepercent = a/1
        w = 1
        x = b/onepercent
        y = c/onepercent
        z = d/onepercent
        return([w,x,y,z])

    plt.rcParams['font.size'] = '16'

    fig = plt.figure(figsize=(7,6))
    axes = plt.subplot(1,1,1)
    ax = plt.axes()
    axes.axis(axis)

    axes.xaxis.set_major_locator(MultipleLocator(xLocator))
    axes.yaxis.set_major_locator(MultipleLocator (yLocator))

    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)

    if datasetname == "cue_conflict":
        plt.plot(positionsData, normalize2(dataA[0], dataA[1]), 'o', linestyle="-", color=c.age1, label="4-6 year-olds")
        plt.plot(positionsData, normalize2(dataB[0], dataB[1]), 'o', linestyle="-", color=c.age2, label="7-9 year-olds")
        plt.plot(positionsData, normalize2(dataC[0], dataC[1]), 'o', linestyle="-", color=c.age3,label="10-12 year-olds")
        plt.plot(positionsData, normalize2(dataD[0], dataD[1]), 'o', linestyle="-", color=c.age4, label="13-15 year-olds")
        plt.plot(positionsData, normalize2(dataE[0], dataE[1]), 'o', linestyle="-", color=c.age5, label="Adults")
        plt.plot(positionsData, normalize2(dataF[0], dataF[1]), 's', linestyle="-", color=c.vgg19, label="VGG-19 (>1M")
        plt.plot(positionsData, normalize2(dataG[0], dataG[1]), '^', linestyle="-", color=c.resnext, label="ResNeXt (>1M")
        plt.plot(positionsData, normalize2(dataH[0], dataH[1]), 'D', linestyle="-", color=c.bitm, label="BiT-M (>10M")
        plt.plot(positionsData, normalize2(dataI[0], dataI[1]), 'p', linestyle="-", color=c.swsl, label="SWSL (>100M")
        plt.plot(positionsData, normalize2(dataJ[0], dataJ[1]), 'h', linestyle="-", color=c.swag, label="SWAG (>1,000M")

    else:
        plt.plot(positionsData, normalize(dataA[0], dataA[1], dataA[2], dataA[3]), 'o', linestyle="-",linewidth=1.5, markersize=8, color=c.age1, label="4-6 year-olds")
        plt.plot(positionsData, normalize(dataB[0], dataB[1], dataB[2], dataB[3]), 'o', linestyle="-",linewidth=1.5, markersize=8, color=c.age2, label="7-9 year-olds")
        plt.plot(positionsData, normalize(dataC[0], dataC[1], dataC[2], dataC[3]), 'o', linestyle="-",linewidth=1.5, markersize=8, color=c.age3,label="10-12 year-olds")
        plt.plot(positionsData, normalize(dataD[0], dataD[1], dataD[2], dataD[3]), 'o', linestyle="-",linewidth=1.5, markersize=8, color=c.age4, label="13-15 year-olds")
        plt.plot(positionsData, normalize(dataE[0], dataE[1], dataE[2], dataE[3]), 'o', linestyle="-",linewidth=1.5, markersize=8, color=c.age5, label="Adults")
        plt.plot(positionsData, normalize(dataF[0], dataF[1], dataF[2], dataF[3]), 's', linestyle="-",linewidth=1.5, markersize=8, color=c.vgg19, label="Vgg-19 (>1M)")
        plt.plot(positionsData, normalize(dataG[0], dataG[1], dataG[2], dataG[3]), '^', linestyle="-",linewidth=1.5, markersize=9, color=c.resnext, label="ResNeXt (>10")
        plt.plot(positionsData, normalize(dataH[0], dataH[1], dataH[2], dataH[3]), 'D', linestyle="-",linewidth=1.5, markersize=8, color=c.bitm, label="BiT-M (>10M")
        plt.plot(positionsData, normalize(dataI[0], dataI[1], dataI[2], dataI[3]),  'p', linestyle="-",linewidth=1.5, markersize=9, color=c.swsl, label="SWSL (>100M")
        plt.plot(positionsData, normalize(dataJ[0], dataJ[1], dataJ[2], dataJ[3]),  'h', linestyle="-",linewidth=1.5, markersize=9, color=c.swag, label="SWAG (>1,00M")

    plt.xlabel(xlabel)
    if datasetname == "cue_conflict":
        plt.xticks([0, 1], ['Original', 'Cue-conflict'])
    elif datasetname == "noise":
        plt.xticks(positionsData, ['0', '0.1', '0.2', '0.35'])
    elif datasetname == "eidolon":
        plt.xticks(positionsData,  ['0', '1', '2', '3'])
    

    plt.ylabel("Normalized classification accuracy")
    plt.tight_layout()
    sns.despine(trim=True)

    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    labels = list(by_label.values())[::-1] #reverse label order
    handles = list(by_label.keys())[::-1] #reverse handle order

    plt.savefig(path, bbox_inches='tight', dpi=150)
    plt.close()

def accuray_delta_plot (results, plotpath):
    plt.rcParams['font.size'] = '15'    
    axis = [0,0,-0.7,0]
    xLocator = 0.1
    yLocator = 0.1

    fig = plt.figure(figsize=(7,6))
    axes = plt.subplot(1,1,1)
    ax = plt.axes()
    axes.axis(axis)
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)

    plot = sns.barplot(x='category',
        y='delta', data=results,
        order=results.sort_values('delta').category, color = 'lightgrey')
    
    ticks = [-0.7,-0.6,-0.5,-0.4, -0.3, -0.2, -0.1, 0]
    plot.set_yticks(ticks)
    plot.set_yticklabels(ticks)  
    plot.set(xlabel=None)
    plt.ylabel('Accuracy delta')  
    plt.xticks(rotation = 90)
    sns.despine(trim=True)
    plt.savefig(plotpath, bbox_inches='tight', dpi=150)
    plt.close()

def plot_confusion_matrix_single(data, plotname,
                          plot_cbar=False, plot_labels=True):
    
    diff_levels = ['_diff_0', '_diff_1','_diff_2', '_diff_3']

    sns.set(color_codes=True)

    fig = plt.figure(figsize = (7,7)) # width x height
 
    sns.set(font_scale=1.2)

    N = 256
    vals = np.ones((N, 4))
    vals[:, 0] = np.linspace(165/256, 1, N)
    vals[:, 1] = np.linspace(30/256, 1, N)
    vals[:, 2] = np.linspace(55/256, 1, N)
    newcmp = ListedColormap(vals)
 
    count = 0
    for d in data:
        ax = sns.heatmap(d, cmap=newcmp.reversed(), annot=False,
                            vmin=0.0, vmax=1.0, linecolor="black", linewidths=1.0,
                            square=True, cbar=False,
                            xticklabels=plot_labels, yticklabels=plot_labels, cbar_kws={"shrink": .8})               

        ax.set_yticklabels(ax.get_ymajorticklabels(), fontsize = 27)
        ax.set_xticklabels(ax.get_xmajorticklabels(), fontsize = 27)

        if plot_labels:
            colnames = list(d.columns)
            rownames = list(d.index.values)
            ax.set_xticklabels(colnames)
            ax.set_yticklabels(rownames)
            # ax.set(xlabel="Presented category", ylabel="Decision")
            ax.set_xlabel("Presented category", fontsize = 30)
            ax.set_ylabel("Decision", fontsize = 30)
        else:
            ax.set(xlabel="", ylabel="")

        fig.set_tight_layout(True)
        plt.savefig(plotname + diff_levels[count], bbox_inches='tight', dpi=200)
        count += 1

def input_vs_robustness_plot(plotname, df_humans, df_models, type = 'sample_size'):

    palette = [c.vgg19, c.resnext, c.bitm, c.swsl, c.swag]
    markers = ["d", "d", "d", "d"]

    legend_elements = [Line2D([0], [0], marker="d",lw = 0, color=c.age1, label='4-6 year-olds',
                            markersize=8),
                    Line2D([0], [0], marker="d",lw = 0, color=c.age2, label='7-9 year-olds',
                            markersize=8),
                    Line2D([0], [0], marker="d", lw = 0, color=c.age3, label='10-12 year-olds',
                            markersize=8),
                        Line2D([0], [0], marker="d", lw = 0, color=c.age4, label='13-15 year-olds',
                            markersize=8),
                    Line2D([0], [0], marker="d", lw = 0, color=c.age5, label='Adults',
                        markersize=8),
                        Line2D([0], [0], color='grey',linestyle= ":", lw=0, label=''),
                        Line2D([0], [0], color='grey',linestyle= ":", lw=1.5, label='minute'),
                        Line2D([0], [0], color='grey',linestyle= "--", lw=1.5, label='eight seconds'), 
                        Line2D([0], [0], color='grey',linestyle= "-.", lw=1.5, label='single second'),
                        Line2D([0], [0], color='grey',linestyle= "-", lw=1.5, label='single fixation')]


    plt.rcParams['font.size'] = '16'

    axis = [10**5.97,10**10, -0.01, 0.75]

    fig = plt.figure(figsize=(12,6))
    axes = plt.subplot(1,1,1)
    ax = plt.axes()
    axes.axis(axis)

    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)

    if type == 'sample_size':
        sns.scatterplot(
            data=df_models, x='samplesize', y='robustness', hue='model', size='parameters',sizes=(200, 2000), palette = palette)
        plt.annotate("VGG-19\n(144M param.)", (10**8.07, .15), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("ResNeXt\n(44M param.)", (10**8.15, .305), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("BiT-M\n(928M param.)", (10**8.47, .53), textcoords="offset points", xytext=(0,-16), size=10, ha = "right")
        plt.annotate("SWSL\n(829M param.)", (10**9.15, .513), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("SWAG\n(645M param.)", (10**9.858, .6), textcoords="offset points", xytext=(0,-16), size=10, ha = "center")
        plt.annotate('New image every ...', (10**6.76, .197,),textcoords="offset points", xytext=(0,-16), size=10,)
        linewidths = [0.5,2.5]
   
    elif type == 'dataset_size':
        sns.scatterplot(
            data=df_models, x='dataset', y='robustness', hue='model', size='parameters',sizes=(200, 2000), palette = palette)
        plt.annotate("VGG-19\n(144M param.)", (10**6.2, .14), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("ResNeXt\n(44M param.)", (10**6.2, .305), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("BiT-M\n(928M param.)", (10**7.32, .53), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("SWSL\n(829M param.)", (10**9.15, .513), textcoords="offset points", xytext=(0,-16), size=10)
        plt.annotate("SWAG\n(645M param.)", (10**9.72, .68), textcoords="offset points", xytext=(0,-16), size=10)
        linewidths = [2.5,0.5]

    xdata_46 = h.get_dataframe_row(df_humans,"4-6")
    ydata_46 = [.434,.434,.434,.434]
    xdata_79 = h.get_dataframe_row(df_humans,"7-9")
    ydata_79 = [.561,.561,.561,.561]
    xdata_1012 = h.get_dataframe_row(df_humans,"10-12")
    ydata_1012 = [.571,.571,.571,.571]
    xdata_1315 = h.get_dataframe_row(df_humans,"13-15")
    ydata_1315 = [.642,.642,.642,.642]
    xdata_adults = h.get_dataframe_row(df_humans,"adults")
    ydata_adults = [.669,.669,.669,.669]

    plt.plot(df_humans['minute'].tolist(), df_humans['robustness'].tolist(), linestyle=":", linewidth=linewidths[0], markersize=8, color='grey')
    plt.plot(df_humans['8_seconds'].tolist(), df_humans['robustness'].tolist(), linestyle="--", linewidth=linewidths[0], markersize=8, color='grey')
    plt.plot(df_humans['second'].tolist(), df_humans['robustness'].tolist(), linestyle="-.", linewidth=linewidths[1], markersize=8, color='grey')
    plt.plot(df_humans['fixation'].tolist(), df_humans['robustness'].tolist(), linestyle="-", linewidth=linewidths[1], markersize=8, color='grey')
    
    for xp, yp, m in zip(xdata_46, ydata_46, markers):
        plt.plot(xp, yp, marker=m, linestyle=":", linewidth=1.5, markersize=8, color=c.age1)

    for xp, yp, m in zip(xdata_79, ydata_79, markers):
        plt.plot(xp, yp, marker=m, linestyle="-", linewidth=1.5, markersize=8, color=c.age2)

    for xp, yp, m in zip(xdata_1012, ydata_1012, markers):
        plt.plot(xp, yp, marker=m, linestyle="-", linewidth=1.5, markersize=8, color=c.age3)

    for xp, yp, m in zip(xdata_1315, ydata_1315, markers):
        plt.plot(xp, yp, marker=m, linestyle="-", linewidth=1.5, markersize=8, color=c.age4)

    for xp, yp, m in zip(xdata_adults, ydata_adults, markers):
        plt.plot(xp, yp, marker=m, linestyle="-", linewidth=1.5, markersize=8, color=c.age5)

    plt.legend([],[], frameon=False)
    plt.xscale("log")
    sns.despine(trim=True)
    plt.xticks( [10**6, 10**7, 10**8, 10**9, 10**10], ['$\mathregular{10^{6}}$','$\mathregular{10^{7}}$','$\mathregular{10^{8}}$','$\mathregular{10^{9}}$','$\mathregular{10^{10}}$'])
    plt.ylabel('OOD robustness')

    if type == 'sample_size':
        plt.xlabel('Sample size [total number of images exposed to; training set x epochs]')
        ax.legend(handles=legend_elements, loc = (0.005, 0.03), frameon = False, ncol = 2 , prop={'size': 10})
    elif type == 'dataset_size':
        plt.xlabel('Dataset size [number of images in training set]')

    plt.savefig(plotname + type, bbox_inches='tight', dpi=150)
    plt.close()

def errorK_multi_boxplot(dfs, dataset, save_path):

    dat = []

    for i in dfs: 

        i = i.reset_index(drop=True)

        i['order'] = ''

        for s, row in i.iterrows():

            if row['condition'] == "Adults vs. DNNs":
                i.iloc[s,7]= '1'
            elif row['condition'] == "7-9 vs. DNNs":
                i.iloc[s,7]= '2'
            elif row['condition'] == "4-6 vs. DNNs":
                i.iloc[s,7]= '3'
            elif row['condition'] == "7-9 vs. Adults":
                i.iloc[s,7]= '4'
            elif row['condition'] == "4-6 vs. Adults":
                i.iloc[s,7]= '5'
            elif row['condition'] == "4-6 vs. 7-9":
                i.iloc[s,7]= '6'
            elif row['condition'] == "DNNs vs. DNNs":
                i.iloc[s,7]= '7'
            elif row['condition'] == "Adults vs. Adults":
                i.iloc[s,7]= '8'
            elif row['condition'] == "7-9 vs. 7-9":
                i.iloc[s,7]= '9'
            elif row['condition'] == "4-6 vs. 4-6":
                i.iloc[s,7]= '10'
        
        i["order"] = pd.to_numeric(i["order"])
        i = i.sort_values(by=['order'], ascending=False)
        dat.append(i)

    if dataset =="eidolon":

        f, ax = plt.subplots(1,4, figsize=(16,6))

        x =[ax[1], ax[2], ax[3]]
        y = [ax[0]]
        z = [ax[0],ax[1], ax[2], ax[3]]

        plot_titles = ["Reach level = 0", "Reach level = 4", "Reach level = 8", "Reach level = 16"]

    elif dataset == "noise":

        f, ax = plt.subplots(1,4, figsize=(16,6))

        x =[ax[1], ax[2], ax[3]]
        y = [ax[0]]
        z = [ax[0],ax[1], ax[2], ax[3]]

        plot_titles = ["Noise level = 0.0","Noise level = 0.1","Noise level = 0.2","Noise level = 0.35"]
    
    elif dataset == "cueconflict":

        f, ax = plt.subplots(1,2, figsize=(8,10))
        x =[ax[1]]
        y = [ax[0]]
        z = [ax[0],ax[1]]

        plot_titles = ["Original","Cue-conflict"]

    flierprops = dict(marker='o', markersize=0)
    custom_xlim = (-.35, 1.1)

    for i in ax: 
        i.xaxis.grid(True)
        i.set_axisbelow(True)
        i.set(ylabel="", xlabel = "Error consistency (Cohen\'s $\kappa$)")

        plt.setp(i, xlim=custom_xlim)

        a = i.get_xgridlines()
        b = a[1]
        b.set_linewidth(2) 

    count = 0
    for a,d in zip (ax, dat):
        sns.boxplot(x="cohens-kappa", y="condition", data=d, orient='h', showmeans = True,meanprops={"marker": "|",
                "markerfacecolor": c.marker_error_box_mean,"markeredgecolor": c.marker_error_box_mean,
                "markersize": "18"},
                    width=.6, palette=c.palette, flierprops= flierprops, ax=a).set_title(plot_titles[count])
        
        sns.stripplot(x="cohens-kappa", y="condition", data=d,
                    size=3.6, palette=c.palette2, linewidth=1, ax=a)
        count += 1

    if dataset =="eidolon":
        y[0].set(ylabel = "Eidolon")
    elif dataset == "noise":
        y[0].set(ylabel = "Salt-and-pepper noise")
    elif dataset == "cueconflict":
        y[0].set(ylabel = "Cue-conflict")

    l = y[0].get_ylabel()
    y[0].set_ylabel(l, fontsize=20)

    y[0].tick_params(
                axis='y',          # changes apply to the y-axis
                which='both',      # both major and minor ticks are affected
                left=False,      # ticks along the bottom edge are off
                top=False,         # ticks along the top edge are off
                labelleft=True) # labels along the bottom edge are off

    y[0].plot([-.8, 1], [3.5, 3.5], lw=1, linestyle = ':', color='gray', clip_on=False)
    y[0].plot([-.8, 1], [6.5, 6.5], lw=1, linestyle = ':', color='gray', clip_on=False)

    for x in x:
        x.tick_params(
            axis='y',         
            which='both',      
            left=False,      
            top=False,         
            labelleft=False) 
        x.plot([-.6, 1], [3.5, 3.5], lw=1,linestyle = ':', color='gray', clip_on=False)
        x.plot([-.6, 1], [6.5, 6.5], lw=1, linestyle = ':', color='gray', clip_on=False)

    custom_xlim = (-.35, 1.1)

    for i in [0,1,2,3]:

        ax[i].spines['top'].set_visible(False)
        ax[i].spines['right'].set_visible(False)
        ax[i].spines['left'].set_visible(False)

        ax[i].set_xlabel('Error consistency (Cohen\'s $\kappa$)')
        ax[i].set_ylabel('')

    f.set_tight_layout(True)
    sns.despine(trim=True, left=True)

    plt.savefig(save_path + dataset, bbox_inches='tight', dpi=300)
    plt.close()


def plot_shapebias(path, df,
                   order_by='humans'):
    ICONS_DIR = '/home/rebushulk/Documents/GitHub/JoV/data_analysis/icons/'
    fontsize = 25
    ticklength = 10
    markersize = 250

    classes = df["object_response"].unique()
    num_classes = len(classes)

    # plot setup
    fig = plt.figure(1, figsize=(12, 12), dpi=300.)
    ax = plt.gca()

    ax.set_xlim([0, 1])
    ax.set_ylim([-.5, num_classes-0.5])

    # secondary reversed x axis
    ax_top = ax.secondary_xaxis('top', functions=(lambda x: 1-x, lambda x: 1-x))

    # labels, ticks
    plt.tick_params(axis='y',
                    which='both',
                    left=False,
                    right=False,
                    labelleft=False)
    ax.set_ylabel("Shape categories", labelpad=60, fontsize=fontsize)
    ax.set_xlabel("Fraction of 'texture' decisions", fontsize=fontsize, labelpad=25)
    ax_top.set_xlabel("Fraction of 'shape' decisions", fontsize=fontsize, labelpad=25)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax_top.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.get_xaxis().set_ticks(np.arange(0, 1.1, 0.1))
    ax_top.set_ticks(np.arange(0, 1.1, 0.1))
    ax.tick_params(axis='both', which='major', labelsize=fontsize, length=ticklength)
    ax_top.tick_params(axis='both', which='major', labelsize=fontsize, length=ticklength)

    # arrows on x axes
    plt.arrow(x=0, y=-1.75, dx=1, dy=0, fc='black',
              head_width=0.4, head_length=0.03, clip_on=False,
              length_includes_head=True, overhang=0.5)
    plt.arrow(x=1, y=num_classes+0.75, dx=-1, dy=0, fc='black',
              head_width=0.4, head_length=0.03, clip_on=False,
              length_includes_head=True, overhang=0.5)

    # icons besides y axis
    ## determine order of icons
    for dmaker in dm.get_young_decision_makers(df):
        if dmaker.plotting_name == order_by:
            df_selection = df.loc[(df["subj"].isin(dmaker.decision_makers))]
            class_avgs = []
            for cl in classes:
                df_class_selection = df_selection.query("category == '{}'".format(cl))
                class_avgs.append(1 - a.shapeB(df=df_class_selection)['shape-bias'])
            sorted_indices = np.argsort(class_avgs)
            classes = classes[sorted_indices]
            break

    # icon placement is calculated in axis coordinates
    WIDTH = 1/num_classes #
    XPOS = -1.25*WIDTH # placement left of yaxis (-WIDTH) plus some spacing (-.25*WIDTH)
    YPOS = -0.5
    HEIGHT = 1
    MARGINX = 1/10 * WIDTH # vertical whitespace between icons
    MARGINY = 1/10 * HEIGHT # horizontal whitespace between icons

    left = XPOS + MARGINX
    right = XPOS + WIDTH - MARGINX

    for i in range(num_classes):
        bottom = i + MARGINY + YPOS
        top = (i+1) - MARGINY + YPOS
        iconpath = os.path.join(ICONS_DIR, "{}.png".format(classes[i]))
        plt.imshow(plt.imread(iconpath), extent=[left, right, bottom, top], aspect='auto', clip_on=False)

    # plot horizontal intersection lines
    for i in range(num_classes-1):
        plt.plot([0, 1], [i+.5, i+.5], c='gray', linestyle='dotted', alpha=0.4)

    columns = ['4-6', '7-9', '10-12', '13-15','adults', 'vgg19', 'resnext', 'bitm', 'swsl', 'swag']
    df_cat_avgs = pd.DataFrame()

    # plot average shapebias + scatter points
    count = 0
    for dmaker in dm.get_young_decision_makers(df):
        if len(dmaker.age_range) > 0:
            df_selection = df.loc[(df['age'].isin(dmaker.age_range))]
        else:
            df_selection = df.loc[(df["subj"].isin(dmaker.decision_makers))]
        result_df = a.shapeB(df=df_selection)
        print(dmaker.plotting_name, result_df)
        avg = 1 - result_df['shape-bias']
        ax.plot([avg, avg], [-1, num_classes], color=dmaker.color)
        class_avgs = []
        for cl in classes:
            df_class_selection = df_selection.query("category == '{}'".format(cl))
            class_avgs.append(1 - a.shapeB(df=df_class_selection)['shape-bias'])
        df_cat_avgs[columns[count]]=class_avgs
        count+=1
        
        ax.scatter(class_avgs, classes,
                    color=dmaker.color,
                    marker=dmaker.marker,
                    label=dmaker.plotting_name,
                    s=markersize,
                    clip_on=False,
                    zorder=3)

    fig.savefig(path)
    plt.close()


def plot_shape_bias_boxplot(path,df):

    columns = ['age1-', 'age2-', 'age3-', 'age4-','age5-', 'vgg19', 
    'resnext101_32x8d', 'BiTM_resnetv2_152x2', 'ResNeXt101_32x16d_swsl', 'swag_regnety_128gf_in1k']
    df_results = pd.DataFrame()
    classes = df["object_response"].unique()

    # plot setup
    fig = plt.figure(1, figsize=(8, 4), dpi=300.)
    ax = plt.gca()
    axes = plt.subplot(1,1,1)
    plt.xticks(rotation=90)
    ax.set_ylabel("shape bias", fontsize=12)
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)

    colors = []
    labels = []
    label_colors = []

    count = 0
    for dmaker in dm.get_young_decision_makers(df):
        if len(dmaker.age_range) > 0:
            df_selection = df.loc[(df['age'].isin(dmaker.age_range))]
        else:
            df_selection = df.loc[(df["subj"].isin(dmaker.decision_makers))]
        class_avgs = []
        for cl in classes:
            df_class_selection = df_selection.query("category == '{}'".format(cl))
            class_avgs.append(1 - a.shapeB(df=df_class_selection)['shape-bias'])
        df_results[columns[count]]=class_avgs
        count+=1
        colors.append(dmaker.color)
        label_colors.append(dmaker.color)
        labels.append(dmaker.plotting_name)

    df_ones = df_results
    df_ones = df_ones*0+1
    df_results =df_ones - df_results

    boxplot = ax.boxplot(df_results
                         , vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=labels,
                         showfliers=False
                          )
    for element, x_axis, color, label_color in zip(boxplot["boxes"], ax.xaxis.get_ticklabels(), colors, label_colors):
        element.set(color=color)
        x_axis.set_color(label_color)
    plt.axhline(y = 1,xmax = .975, color = 'black',linestyle=':',linewidth=1, alpha = 0.3)
    sns.despine(trim=True)
    plt.subplots_adjust(bottom=0.4)
    plt.ylabel('Shape bias')
    fig.savefig(path)
    plt.close()
