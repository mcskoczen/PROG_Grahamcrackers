
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

class Computer:
 def __init__(self, branch, host, cpu_total):
    self.branch = branch
    self.host = host
    self.cpu_total = cpu_total

d = {}
for x in range(3):
  df = pd.read_csv("cpu" + str(x) + ".csv")
  
  d[x] = df
#creating a loop to read files and assign them to dataframes with a value of x where x is the number of files


listOfWorkstations = []

length = len(df)
for index in range(length):
    listOfWorkstations.append(Computer(df.loc[index].enrichment_branch_name, df.loc[index].beat_hostname, df.loc[index].system_cpu_total_pct))


outliers_fraction = 10/162 

print(d[0])
print(d[1])
print(d[2])
