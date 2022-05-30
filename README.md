# Data and code from "The developmental trajectory of object recognition robustness: children are like small adults but unlike big deep neural networks

![This is an image](https://github.com/wichmann-lab/robustness-development/blob/main/figures/color_theme.png)

This repository contains data and code from the Paper "The developmental trajectory of object recognition robustness: children are like small adults but unlike deep neural networks". In this paper we conducted a series of psychophysical experiments to investigate the developmental trajectory of object recognition robustness. We tested children and adults (aged 4–36) on distorted greyscale ImageNet images and compared their performance with various deep neural networks (DNNs). We find that object recognition robustness emerges early in develoment and that children employ adult-like strategies to recognise images. Furthermore, we find that humans—compared to current robust DNNs— need relatively little external data in order to achieve high object recognition robustness. 

The methods used in this study are adapted from a series of psychophysical experiments conducted by Geirhos and colleagues ([2018](https://papers.nips.cc/paper/2018/file/0937fb5864ed06ffb59ae5f9b5ed67a9-Paper.pdf), [2019](https://arxiv.org/pdf/1811.12231.pdf)). Model evaluation and data analysis was implemented by adapting code from the [modelvshuman](https://github.com/bethgelab/model-vs-human) Python-toolbox.

Please feel free to contact me at lukas.s.huber@unibe.ch or open an issue in case there is any question! 

This README is structured according to the repo's structure: one section per subdirectory (alphabetically).

## code

The `code/` directory contains the code for the psychophysical experiment. We programmed the experiment’s interface with the [Psychopy library](https://doi.org/10.3758/s13428-018-01193-y). Please note that due to copy right issues, images are not publicity available on gitHub. But don't hesitate to contact me and I will be happy to share all the employed images in order to make the code work as it is. 

## data 

The `data/` directory contains the human- as well as the DNN data for all three conducted experiments (`data/eidolon/`, `data/noise/`, and `data/cue_conflict`). Each `.csv` file contains the data from a particular age group (4–6, 7–9, 10–12, 13–15, and adults) or a particular DNN ([VGG-19](https://arxiv.org/abs/1409.1556), [ResNeXt](https://openaccess.thecvf.com/content_cvpr_2017/papers/Xie_Aggregated_Residual_Transformations_CVPR_2017_paper.pdf), [BiT-M](https://arxiv.org/pdf/1912.11370.pdf), [SWSL](https://arxiv.org/pdf/1905.00546.pdf), and [SWAG](https://arxiv.org/pdf/2201.08371.pdf)) . The subdirectory `error_consistency/` contains the raw cohens-kappa for all observers and DNNs used in the error-consistency analysis (compare [Geirhos et al. 2020](https://proceedings.neurips.cc/paper/2020/hash/9f6992966d4c363ea0162a056cb45fe5-Abstract.html)).

Every `.csv` data file has a header with the bold categories below, here's what they stand for:

- __subj__: For DNNs; name of the network. For human observers; subject number. Note that for human observers subjects are not numbered continuously within one experiment, but across experiments.
- __trial__: Trial number
- __rt__: For human observers: reaction time. For DNNs; blank.
- __object_response__: The response given by the observer. I.e., the category which the observer "thinks" corresponds to the shown image.
- __category__: The presented (ground truth) category.
- __imagename__:  E.g., `1111_eid_hum_0_keyboard_40_n04505470_2570.png`

This is a concatenation of the following information (separated by '_'):

1. A number (just ignore it)
2. Experiment ("eid" for eidolon, "snp" for salt-and-pepper noise, and "cc" for cue-conflict
3. Observer-type ("hum" for human observer and "DNN" for deep neural network)
4. Difficulty level—reach parameter in the eidolon experiment (0, 4, 8, 16); percentage of flipped pixels in the noise experiment (0, 0.1, 0.2, 0.35); original (0) vs cue-conflict (1) image in the cue-conflict experiment.
5. Presented category (ground truth)
6. A number (just ignore it)
7. image identifier in the form a_b.JPEG (or a_b.png), with a being the WNID (WordNet ID) of the corresponding synset and b being an integer

Note that for cue-conflict images only information 1–5 is given and 6 refers to the textute and shape of the image. E.g., `1111_cc_hum_1_airplane1-clock1.png` idicates that this is an image featuring shape information of the category _airplane_ and texture information of the category _clock_.

## data_analysis

Each script in the `data_analysis/` directory corresponds to an analysis reported in the paper. All plots reported in the results section of the paper can be generated with these scripts and are stored in the `figures/` directory.

## figures

The `figures/` directory contains all plots reported in the results section of the paper and can be generated using the code from the `data_analysis/` directory.

## citation

@article{huber2022developmental,
  title={The developmental trajectory of object recognition robustness: children are like small adults but unlike big deep neural networks},
  author={Huber, Lukas S and Geirhos, Robert and Wichmann, Felix A},
  journal={arXiv preprint arXiv:2205.10144},
  year={2022}
}

