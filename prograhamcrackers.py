import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import math

for num in range(1):
  df = pd.read_csv("computer" + str(num) + ".csv")
  
  #creating a loop to read files and assign them to dataframes with a value of x where x is the number of files
  #The loop is unnecessary if you aren't going to do things a bunch of times with each thing
  
  minimum = df['X_timestamp'].min() * 0.0001
  maximum = df["X_timestamp"].max() * 0.0001
  minimum = round(minimum, 3)
  maximum = round(maximum, 3)
  timestamp = "between " + str(minimum) + " and " + str(maximum)

  length = len(df)

  N = int(math.sqrt(length - 1)) 
  # N is the square root of the number of workstations, this is the variable to be changed based on the number of workstations when being scaled up for larger production
  # We want N to be an integer to simplify the math being done later
  
  w = length % N
  if w > 0:
    N = N + 1
  #if the number of workstations isn't a perfect square, then we adjust for that by acting as if it is a subset of a larger square

  nameslist = df.columns
  #creating a list of all the names of the columns

  numberofcolumns = len(nameslist)
  #finding how many columns there are

  df.insert(numberofcolumns, 'HBOS', [0.0]*length)
  #creating a new column in the dataframe called HBOS

  for varindex in range(4, numberofcolumns):
    
    df.sort_values(by = nameslist[varindex], ascending = True)
    #sorting the dataframe by the values of the dataframe

    for x in range(length):
     a = int(x/N)

     if x % N != 0:
       a + 1
     if x == 0:
       a + 1
     #determining which bin we're in
     
     b = a * N
     #setting the endpoint of the bin
     
     c = b - N
     #setting the beginning of the bin


     bad = N * N
     if (b == bad):
       b = length -1
       c = length % N
       c = length - c
      #in order to account for the last bin being too short, we make sure c and t are both the correct value for the final bin
     
     
     g = df.iat[b, varindex]
     j = df.iat[c, varindex]
     k = g - j

     if k <= 0 :
       print(g)
       print(j)
     
     while k == 0:
       b = b + 1
       g = df.iat[b, varindex]
       k = g - j

     z = df.at[x, "HBOS"] + math.log10(k/N)
     #doing the math to find the HBOS vallue by takin the base 10 logarithm of N times the difference of the values 
     #of the end of the bin and the beginning of the bin and adding it to the previous value of the HBOS algorithm
         
     df.at[x, "HBOS"] = z

  print("This is for the time interval " + timestamp)
  #df.to_csv('HBOS_topten_fortime' + timestamp + '.csv')
  