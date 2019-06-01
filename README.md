# GPADRlex: Grouped Phrasal Adverse Drug Reaction lexicon

This repository contains supporting data and code used in our paper titled **"GPADRlex: Grouped Phrasal Adverse Drug Reaction lexicon"** that is submitted at **"2019 IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC 2019) "**.

## Files/Folders details

#### Data/grouped_phrasal_ADR_lexicon:

GPADRlex consists of 19,585 phrasal ADRs compiled from FAERS and we grouped the phrases representing similar ADRs together based on semantic similarity using agglomerative hierarchical clustering. This folder contains GPADRlex for different values of k (number of clusters).

#### Data/benchmark_clusters.txt
This file contains benchmark lexicon used in this study. Benchmark lexicon lexicon consist of 890 hand curated groups derived from a subset of ADR lexicon compiled by
Nikfarjam et al.. Each line consist of all the phrases that represent the similar ADR and are grouped together.

#### Data/FAERS_all_ADRs.csv
This file contains a large phrasal ADR lexicon containing 19,585 phrasal ADRs, that we have compiled ADR reported in FAERS.

#### src/get_nclusters.py
This file contains a python script for generating user-defined number of clusters.

## Instruction for using src/get_nclusters.py

Perform the following steps to run the get_nclusters.py
1) clone the GPADRlex with ```git clone https://github.com/HammadFarooq/GPADRlex.git```
2) Download the distance matrix (3.1 GB) from the drive [link](https://drive.google.com/open?id=14EPdGqJe32nGT9Eq14NBDdHBFNMCrYsz) in GPADRlex/Data folder
3) move to "GPADRlex/src" folder with ```cd GPADRlex/src```
4) run the command ```python get_n_clusters.py "single" 100```. where "single" is the linkage criteria and 100 is the value of k (number of clusters).   Linkage can be one of the following: 'single', 'complete', 'average' ,'weighted', 'centroid', 'median' and 'ward'. 

