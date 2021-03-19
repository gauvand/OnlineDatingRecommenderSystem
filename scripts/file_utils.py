#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Python file utilities for graph mining final project

Created on Thu Mar 18 21:51:12 2021

@author: gauravanand
"""

import os 
import csv

def stack_files(data_dir,output_dir):
    '''
    Stacks multiple files to return the original full graph data
    
    '''
    full_data = []
    for file in os.listdir(data_dir):
        with open(f"{data_dir}/{file}") as f:
            full_data.extend(list(map(lambda x: x\
                                 .rstrip()\
                                     .split('\t'),\
                                         f.readlines())))
    with open(f'{output_dir}/full_data.txt','w') as datafile:
        full_data_writer = csv.writer(datafile, delimiter=',')
        for line in full_data:
            full_data_writer.writerow(line)
    print(f'Stacked data files at {output_dir}')
    
if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    data_dir = os.path.join(dirname,'..','raw_data')
    output_dir = os.path.join(dirname,'..','raw_data')
    stack_files(data_dir,output_dir)