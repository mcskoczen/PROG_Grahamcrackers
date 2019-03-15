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

topten= {}
for x in range(1):
  df = pd.read_csv("cpu" + str(x) + ".csv")
  
  #creating a loop to read files and assign them to dataframes with a value of x where x is the number of files
  #The loop is unnecessary if you aren't going to do things a bunch of times with each thing
  
  timestamp = str(df['X_timestamp'].min()) + " - " + str(df['X_timestamp'].max())
  
  #var0 = cpu_total

  listOfWorkstations = []

  length = len(df)
  N = int(math.sqrt(length - 1)) 
  w = length % N
  if w > 0:
    N = N + 1
  # N is the square root of the number of workstations, this is the variable to be changed based on the number of workstations when being scaled up for larger production
  
  HBOS = [0.0] * length

  #for index in range(length):
    #listOfWorkstations.append(Computer(df.loc[index].enrichment_branch_name, df.loc[index].beat_hostname, df.loc[index].system_cpu_total_pct, HBOS = 0))
    #pass
    #remember to add all of the calls to the dataframe for each variable we use

  nameslist = [df.columns]
  numberofvariables = len(nameslist)

  for stuff in range(5, numberofvariables + 1):
    df.sort_values(by = nameslist[stuff])
    for x in range(length):
     b = int(x/N) + 1
     c = b * N
     HBOS[x] = HBOS[x] + math.log10(N*(df[c - 1][stuff] - df[0][stuff]))
    
  df['HBOS'] = HBOS
  print(df.HBOS)
  print(timestamp)
  #df.to_csv('HBOS_topten_fortime.csv')
  