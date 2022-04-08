import pandas as pd

import helper as h
import plotting as p

def accuracy_delta (age_groups, plotname = '_accuracy_delta_plot'):

    # preperation
    PLOT_PATH = h.get_plot_path()
    categories = h.get_category_lables()
    df_results = pd.DataFrame(columns = ['category', age_groups[0], age_groups[1]])
    df_results['category'] = categories
    columns = age_groups

    # get data
    dfs = h.get_df_for_delta(age_groups)

    # analyse category-wise accuracy and calculate delta
    colum = 0
    for df in dfs:
        row = 0
        for cat in categories:
            df_cat = df.loc[df['category'] == cat]
            df_results.at[row,columns[colum]]=h.get_acc(df_cat)
            row += 1
        colum += 1
    df_results['delta'] =df_results[age_groups[0]] - df_results[age_groups[1]]

    # print exact numbers for accuracies and delta
    print('category-wise accuracy and delta:\n',df_results)

    # plotting
    p.accuray_delta_plot(df_results, (PLOT_PATH + 'accuracy/' +plotname + age_groups[0]+ '_' + age_groups[1]))

if __name__ == "__main__":
    accuracy_delta(age_groups = ['4_6', 'adults'], plotname="delta_plot")