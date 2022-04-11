import pandas as pd
import numpy as np
from copy import deepcopy

def sixteen_class_accuracy(df):
    """Return accuracy of responses for one data frame."""
    accuracy = len(df.loc[df.object_response == df.category]) / len(df)
    result_dict = {"16-class-accuracy": accuracy}
    return result_dict


def confusion_matrix(df, categories):
    """Return confusion matrix for one data frame."""

    df = deepcopy(df)
    c = categories

    df['object_response'] = pd.Categorical(df.object_response,
                                            categories=c)

    confusion_matrix = pd.crosstab(df['object_response'], df['category'],
                                    dropna=False)

    confusion_matrix = (100.0*confusion_matrix.astype('float') / confusion_matrix.sum(axis=0)[np.newaxis, :])/100
    return confusion_matrix



def get_texture_category(imagename):
    """Return texture category from imagename.
    e.g. 'XXX_dog10-bird2.png' -> 'bird
    '"""
    assert type(imagename) is str

    # remove unneccessary words
    a = imagename.split("_")[-1]
    # remove .png etc.
    b = a.split(".")[0]
    # get texture category (last word)
    c = b.split("-")[-1]
    # remove number, e.g. 'bird2' -> 'bird'
    d = ''.join([i for i in c if not i.isdigit()])
    return d

def shapeB(df):
    """Return dictionary containing fraction of
    correct shape- and texture-responses and shape
    bias, which is the proportion of correct shape
    reponses out of all correct responses."""

    df = df.copy()
    df["correct_texture"] = df["imagename"].apply(get_texture_category)
    df["correct_shape"] = df["category"]

    # remove those rows where shape = texture, i.e. no cue conflict present
    df2 = df.loc[df.correct_shape != df.correct_texture]
    fraction_correct_shape = len(df2.loc[df2.object_response == df2.correct_shape]) / len(df)
    fraction_correct_texture = len(df2.loc[df2.object_response == df2.correct_texture]) / len(df)

    shape_bias = fraction_correct_shape / (fraction_correct_shape + fraction_correct_texture)

    result_dict = {"fraction-correct-shape": fraction_correct_shape,
                    "fraction-correct-texture": fraction_correct_texture,
                    "shape-bias": shape_bias}
    return result_dict
