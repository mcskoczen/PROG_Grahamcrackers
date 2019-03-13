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
for x in range(3):
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
  df['HBOS'] = 0

  for index in range(length):
    listOfWorkstations.append(Computer(df.loc[index].enrichment_branch_name, df.loc[index].beat_hostname, df.loc[index].system_cpu_total_pct, HBOS = 0))
    pass
    #remember to add all of the calls to the dataframe for each variable we use

  nameslist = df.columns
  numberofvariables = len(nameslist)

  for stuff in range(numberofvariables - 1):
    #variable[stuff] -> math thingies
    df.sort_values(by = nameslist[stuff])
    for x in range(13):
      a = df.loc[12][stuff]
      b = df.loc[0][stuff]
      c = df.loc[x][numberofvariables]
      d = a - b
      e = N * d
      f = c + math.log10(e)
      df[x][numberofvariables] = f
      #df.loc[x].HBOS =  c + math.log10(N*(a - b))
    for x in range(13,26):
      #df[x].HBOS = df[x].HBOS + math.log10(N*(df[25].variablename - df[13].variablename))
      pass
    for x in range(26,39):
      #df[x].HBOS = math.log10 
      pass
    pass
  print(df)
  print(timestamp)
  print(nameslist)
  #df.to_csv('HBOS_topten_fortime.csv')
  