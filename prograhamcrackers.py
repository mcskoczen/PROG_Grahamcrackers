import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import math

pd.set_option('display.max_rows', 2000)
#pd.set_option('display.max_columns', 30)

for file_index in range(1):
  df = pd.read_csv("computer" + str(file_index) + ".csv")
  
  #creating a loop to read files and assign them to dataframes with a value of x where x is the number of files
  #The loop is unnecessary if you aren't going to read in multiple sheets consecutively
  
  minimum = df['X_timestamp'].min() * 0.0001
  maximum = df["X_timestamp"].max() * 0.0001
  minimum = round(minimum, 3)
  maximum = round(maximum, 3)
  timestamp = "between " + str(minimum) + " and " + str(maximum) + str(file_index)

  row_count = len(df)
  urow_count = row_count - 1
  
  N = int(math.sqrt(row_count))
  # N is the square root of the number of workstations, this is the variable to be changed based
  # on the number of workstations when being scaled up for larger production.
  # We want N to be an integer to simplify the math being done later
  # N is how many values go in each bin, except when there are > N of same value for a variable 
  
  w = row_count / N
  #The modulo function divides row_count by N, returns remainder, if perfect square, will be 0. else, will be > 0.
  if w != N :
    N = N + 1 
  #if the number of workstations isn't a perfect square, then we adjust for that by acting as if it is a subset of a larger square
  Reset_Val = N

  list_of_columns = df.columns
  #creating a list of all the names of the columns

  column_count = len(list_of_columns)
  #finding how many columns there are, here 17
  
  df.insert(column_count, 'HBOS', [0.0]*row_count)
  #creating a new column in the dataframe called HBOS, populating with 0.0
  for var_index in range(3, column_count):
    
    df = df.sort_values(by = list_of_columns[var_index], ascending = True)
    #sorting the dataframe by the values of the variable in ascending order

    N = Reset_Val
    bin_start = 0
    bin_end = N - 1
    #df.to_csv('HBOS for' + list_of_columns[var_index - 1])

    for x in range(row_count):
     if df.iat[x, var_index] == 0:
       bin_start = x + 1
       bin_end = bin_end + 1
       continue
     
     if x > bin_end:
       bin_start = bin_end
       N = Reset_Val
       bin_end = bin_start + N
     #setting the beginning and end of the bin
     #bin_start is the workstation index whose value will be used in calculations
     #we always want the bin to contain 13 values, barring certain circumstances

     if bin_end > (urow_count):
       bin_end = urow_count
       N = bin_end - bin_start
     #unless the last bin would try to call on values that don't exist
     #setting the endpoint of the bin, minus 1 accounts for us having a row 0
     #bin_end is the workstation index whose value will be used in calculations
     
     g = df.iat[bin_end, var_index]
     j = df.iat[bin_start, var_index]

     k = g - j

     if k == 0:
       print("The problem bin is in the column labelled " + list_of_columns[var_index])
       print("It starts at workstation " +str(bin_start) + " with a value of " + str(j))
      

     while k == 0:
       bin_end = bin_end + 1
       N = N + 1
       
       g = df.iat[bin_end, var_index]
       j = df.iat[bin_start, var_index]
       k = g - j

       check = df.iat[urow_count, var_index]
       if g == check:
         bin_end = urow_count
         N = bin_end - bin_start

       if k != 0:
         print("and ends at workstation "+ str(bin_end)+ " with a value of " + str(g))    
     
     y = math.log10(k/N)
     z = df.at[x, "HBOS"]
     H_val = y + z
     #doing the math to find the HBOS vallue by taking the base 10 logarithm of N times the difference of the values 
     #of the end of the bin and the beginning of the bin and adding it to the previous value of the HBOS algorithm
     df.at[x, "HBOS"] = H_val

  df = df.sort_values(by = "HBOS", ascending = False)
  print(df)
  print("This is for the time interval " + timestamp)
  df.to_csv('HBOS_topten_fortime' + timestamp + '.csv')
  