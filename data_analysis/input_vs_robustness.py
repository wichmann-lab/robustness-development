import pandas as pd
from complements import plotting as p
from complements import helper as h


# Create dictonary with model details. Information regarding
# 'datasetsize', 'epochs', and 'parmaters' is taken from the
# respective articles (see main paper for references).
# 'robustness' is calculated based the evaluation on our ood 
# datasets. 'samplesize' is calculated by 'dataset' times 'epochs'
# (except for BiT-M---see table 3, appendix A.4 in the main paper.)
dict_models = {'model': ['Vgg-19', 'ResNeXt', 'BiT-M', 'SWSL', 'SWAG'],
    'dataset': [1280000, 1280000, 14000000, 940000000, 3600000000],
    'epochs': [74, 90, 31, 30, 2],
    'parameters': [144, 44, 928, 829, 645],
    'robustness': [.135, .281, .513, .494, .659],
    'samplesize': [94720000,115200000, 420000000,978400000, 7200000000]}

df_models = pd.DataFrame(data=dict_models)

# Create dict with human details. See table 2 in appendix A.4 in the
# main paper.
dict_humans = {'age': ['4-6', '7-9', '10-12', '13-15', 'adults'],
    'robustness': [.434, .561, .571, .642, .669],
    'minute': [4240000,6760000,9520000,12990000,33730000],
    '8_seconds': [10600000,16900000,23800000,32430000, 84230000],
    'second': [84830000,135150000,190390000,259430000,674550000],
    'fixation': [254490000,405440000,571160000,779120000, 2023650000]}

df_humans = pd.DataFrame(data=dict_humans)

PLOT_PATH = h.get_plot_path()

def input_vs_robustness(plotname, df_humans, df_models, types):

    for type in types: 
        p.input_vs_robustness_plot(plotname, df_humans, df_models, type)

if __name__ == "__main__":
    types = ['sample_size', 'dataset_size']
    input_vs_robustness(PLOT_PATH + '/input_vs_robustness/', df_humans, df_models, types)
