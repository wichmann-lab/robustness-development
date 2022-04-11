from dataclasses import dataclass
import fnmatch
from matplotlib.lines import Line2D

from . import colors as c

"""
Define decision makers for shape bias plots
"""

@dataclass
class DecisionMaker:
    age_range: any
    name_pattern: any
    df: any
    color: any = "grey"
    marker: str = "o"
    plotting_name: str = None

    def __post_init__(self):


        self.name_pattern = [self.name_pattern]

        self.decision_makers = []
        for subj in self.df.subj.unique():

            for pattern in self.name_pattern:
                if fnmatch.fnmatch((str(subj).split("-")[0] + "-"), pattern): # changed - before: if fnmatch.fnmatch(subj, pattern)
                    self.decision_makers.append(subj)

def get_young_decision_makers(df):

    d = []

    d.append(DecisionMaker(age_range = [],
                           name_pattern="vgg19-",
                           color=c.vgg19, marker="s", df=df,
                           plotting_name="VGG-19 (>1M)"))
    d.append(DecisionMaker(age_range = [],
                           name_pattern="resnext101_32x8d-",
                           color=c.resnext, marker="^", df=df,
                           plotting_name="ResNeXt (>1M)"))
    d.append(DecisionMaker(age_range = [],
                           name_pattern="BiTM_resnetv2_152x2-",
                           color=c.bitm, marker="D", df=df,
                           plotting_name="BiT-M (>10M)"))
    d.append(DecisionMaker(age_range = [],
                           name_pattern="ResNeXt101_32x16d_swsl-",
                           color=c.swsl, marker="p", df=df,
                           plotting_name="SWSL (>100M)"))
    d.append(DecisionMaker(age_range = [],
                           name_pattern="swag_regnety_128gf_in1k-",
                           color=c.swag, marker="h", df=df,
                           plotting_name="SWAG (>1,000M)"))
    d.append(DecisionMaker(age_range = [4,5,6],
                           name_pattern="age1-",
                           color=c.age1, marker="o", df=df,
                           plotting_name="4-6 year-olds"))
    d.append(DecisionMaker(age_range = [7,8,9],
                           name_pattern="age2-",
                           color=c.age2, marker="o", df=df,
                           plotting_name="7-9 year-olds"))
    d.append(DecisionMaker(age_range = [10,11,12],
                           name_pattern="age3-",
                           color=c.age3, marker="o", df=df,
                           plotting_name="10-12 year-olds"))
    d.append(DecisionMaker(age_range = [13,14,15],
                           name_pattern="age4-",
                           color=c.age4, marker="o", df=df,
                           plotting_name="13-15 year-olds"))
    d.append(DecisionMaker(age_range = [i for i in range(20,40)],
                           name_pattern="age5-",
                           color=c.age5, marker="o", df=df,
                           plotting_name="Adults"))

    return d