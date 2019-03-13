
# Author: Yue Zhao <yuezhao@cs.toronto.edu>
# License: BSD 2 clause

from __future__ import division
from __future__ import print_function

import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(
  os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

# suppress warnings for clean output
import warnings
warnings.filterwarnings("ignore")

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import math

class Computer:
 def __init__(self, branch, host, cpu_total, HBOS):
    self.branch = branch
    self.host = host
    self.cpu_total = cpu_total
    self.HBOS = HBOS

d = {}
topten= {}
for x in range(3):
  df = pd.read_csv("cpu" + str(x) + ".csv")
  
  d[x] = df
#creating a loop to read files and assign them to dataframes with a value of x where x is the number of files

#var0 = cpu_total

listOfWorkstations = []

length = len(df)
N = int(math.sqrt(length - 1)) 
w = length % N
if w > 0:
  N = N + 1

# N is the square root of the number of workstations, this is the variable to be changed based on the number of workstations when being scaled up for larger production
for index in range(length):
    listOfWorkstations.append(Computer(df.loc[index].enrichment_branch_name, df.loc[index].beat_hostname, df.loc[index].system_cpu_total_pct, HBOS = 0))

numberofvariables = 1
#create a thing where we call a number to get a string where string is the names of variables
for stuff in range(numberofvariables):
  #variable[stuff] -> math thingies
  #sort by value
  for x in range(13):
    #object[x].HBOS =  object[x].HBOS + log10(N*(object[12].var+str(stuff) - object[0].variablename))
    pass
  for x in range(13,26):
    #object[x].HBOS = object[x].HBOS + log10(N*(object[25].variablename - object[13].variablename))
    pass
  for x in range(26,39):
    #object[x].variablename = log 
    pass 
  pass

outliers_fraction = 10/162 

print(d[0])
print(d[1])
print(d[2])

print(d[0].system_cpu_system_pct)