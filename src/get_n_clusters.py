#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy.spatial.distance import squareform
import scipy.cluster.hierarchy as hcl
import pandas as pd
import sys

# get_n_clusters() takes three argumets: distance_matrix, hierarcal_linkage_output, n_clsuters and return a python dictionary with n key value pairs.

def get_n_clusters(distance_matrix,hierarcal_linkage_output, n_clsuters):
    cluster_dict={}
    for i in range(len(distance_matrix)):
        cluster_dict[i]=[i]
    count=len(distance_matrix)
    if len(cluster_dict.keys())==n_clsuters:
        return cluster_dict
    for i, merge in enumerate(hierarcal_linkage_output):
        if merge[0]==merge[1]:
                cluster_dict[int(count)]=cluster_dict[int(merge[0])]
                del cluster_dict[int(merge[0])]
        else:
            cluster_dict[int(count)]=cluster_dict[int(merge[0])]+cluster_dict[int(merge[1])]
            del cluster_dict[int(merge[0])]
            del cluster_dict[int(merge[1])]
        count+=1
        if len(cluster_dict.keys())==n_clsuters:
            return cluster_dict
    return cluster_dict



def main(argv):

    linkage_criteria,n=argv
    
    # linkage_criteria='single'
    # n=100
    
    #load FAERS_all_ADRs.csv
    side_effect_df=pd.read_csv('../Data/FAERS_all_ADRs.csv',sep=',',index_col=0)
    
    # load distance matrix
    loaded=np.load('../Data/distance_matrix_with_normaliation_all_fda.npz')
    distance_matrix=loaded['arr_0']
    condensed_distance_matrix=squareform(distance_matrix)
    Z=hcl.linkage(condensed_distance_matrix,str(linkage_criteria))
    n_clusters=get_n_clusters(distance_matrix,Z,n)
    
    # creating output dataframe
    cluster_df=pd.DataFrame(columns=['sideefects'])
    for key,value in n_clusters.items():
        sideefects=''
        for cluster in value:
            sideefects+=', '+side_effect_df.iloc[int(cluster)]['sideefect']
        cluster_df=cluster_df.append({'sideefects':sideefects},ignore_index=True)
    cluster_df.to_csv('../Data'+str(n)+'_clusters.csv')
    



if __name__ == "__main__":
    main(sys.argv[1:])





