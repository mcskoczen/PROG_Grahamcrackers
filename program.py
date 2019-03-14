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
  N = 13

  for stuff in range(5, numberofvariables + 1):
    df.sort_values(by = nameslist[stuff])
    for x in range(13):
     HBOS[x] = HBOS[x] + math.log10(N*(df[12][stuff] - df[0][stuff]))
    for x in range(13,26):
      HBOS[x] = HBOS[x] + math.log10(N*(df[25][stuff] - df[13][stuff]))
    for x in range(26,39):
      HBOS[x] = HBOS[x] + math.log10(N*(df[38][stuff] - df[26][stuff]))
    for x in range(39,52):
      HBOS[x] = HBOS[x] + math.log10(N*(df[51][stuff] - df[39][stuff]))
    for x in range(52,65):
      HBOS[x] = HBOS[x] + math.log10(N*(df[64][stuff] - df[52][stuff]))
    for x in range(65,88):
      HBOS[x] = HBOS[x] + math.log10(N*(df[87][stuff] - df[65][stuff]))
    for x in range(88,101):
      HBOS[x] = HBOS[x] + math.log10(N*(df[100][stuff] - df[88][stuff]))
    for x in range(101,114):
      HBOS[x] = HBOS[x] + math.log10(N*(df[113][stuff] - df[101][stuff]))
    for x in range(114,127):
      HBOS[x] = HBOS[x] + math.log10(N*(df[126][stuff] - df[114][stuff]))
    for x in range(127,140):
      HBOS[x] = HBOS[x] + math.log10(N*(df[139][stuff] - df[127][stuff]))
    for x in range(140,153):
      HBOS[x] = HBOS[x] + math.log10(N*(df[152][stuff] - df[140][stuff]))
    for x in range(153,161):
      HBOS[x] = HBOS[x] + math.log10(N*(df[160][stuff] - df[153][stuff]))

  df['HBOS'] = HBOS
  print(df.HBOS)
  print(timestamp)
  #df.to_csv('HBOS_topten_fortime.csv')
  