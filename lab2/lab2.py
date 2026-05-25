#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:07:09 2026

@author: robert
"""
import sys 
from Bio.SeqUtils import nt_search # returns the searched sequence and all results including intersecting ones 

with open("input2.txt", "r") as fl:
    s=fl.readline().strip()
    t=fl.readline().strip()
    
if len(s) > 1000 or len(t) > 1000:
    print('the condition is not satified')
    sys.exit(1)
    

results=nt_search(s, t)
final= [str(i) for i in results[1:]]
print(" ".join(final))