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
  df = pd.read_csv("computer" + str(x) + ".csv")
  
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

  #for index in range(length):
    #listOfWorkstations.append(Computer(df.loc[index].enrichment_branch_name, df.loc[index].beat_hostname, df.loc[index].system_cpu_total_pct, HBOS = 0))
    #pass
    #remember to add all of the calls to the dataframe for each variable we use

  nameslist = [df.columns]
  #creating a list of all the names of the columns
  numberofcolumns = len(nameslist)
  #finding how many columns there are
  df.insert(numberofcolumns, 'HBOS', [0]*length)
  #creating a new column in the dataframe called HBOS

  for stuff in range(4, numberofcolumns - 1):
    df.sort_values(by = nameslist[stuff])
    #sorting the dataframe by the values of the dataframe
    for x in range(length):
     b = int(x/N) + 1
     #determining which bin we're in
     c = b * N
     #setting the endpoint of the bin
     t = c - N
     #setting the beginning of the bin
    if (c == N*N):
      #in order to account for the last bin being too short, ensuringg c and t are both the correct value
      c = length
      t = N * (N - 1)
    df.iloc[x,df.columns.get_loc('HBOS')] = df[x]['HBOS'] + math.log10(N*(df[c][stuff] - df[t][stuff]))

  print(df.HBOS)
  print("This is for the time interval: " + timestamp)
  #df.to_csv('HBOS_topten_fortime' + timestamp + '.csv')
  