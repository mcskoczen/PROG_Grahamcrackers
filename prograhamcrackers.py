import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import math

pd.set_option('display.max_rows', 2000)

for file_index in range(1,4):
  #df = pd.read_csv("computer" + str(file_index) + ".csv")
  df = pd.read_csv("Ver" + str(file_index) + ".csv")
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

  list_of_columns = df.columns.values
  #creating a list of all the names of the columns

  column_count = len(list_of_columns)
  #finding how many columns there are, here 17
  df.insert(column_count, "HBOS", [0.0]*row_count)
  df.insert(column_count + 1, 'Heights', [0.0]*row_count)

  for var_index in range(3, column_count):
    #print("this is the dataframe after column: " + str(var_index - 1))
    df = df.sort_values(by = list_of_columns[var_index], ascending = True)
    df = df.reset_index(drop = True)
    #sorting the dataframe by the values of the variable in ascending order
    
    N = Reset_Val
    bin_start = 0
    bin_end = N - 1
    #Setting the initial parameters and ensuring we always go into the loop with the correct numbers

    for x in range(row_count):
     if df.iat[x, var_index] == 0:
       bin_start = x + 1
       bin_end = bin_end + 1
       #this is for the specific use case where the anomoly detection is being applied on computers, where a value
       #of zero doesn't actually mean any value of anything, necesasarily, and instead means the computer isn't doing
       #anything
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
     #like if the last bin would try to call on values that don't exist
     #setting the endpoint of the bin
     #bin_end is the workstation index whose value will be used in calculations
     
     g = df.iat[bin_end, var_index]
     j = df.iat[bin_start, var_index]

     k = g - j
      

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
  
     
     y = N/k
     df.at[x, "Heights"] = y
     #Finding the height of the histograms and assigning each variable that height
    max_height = max(df.Heights)
    #determining the maximum height of a bin to normalize the height of every bin
    for x in range(row_count):
      if df.iat[x, var_index] == 0:       
       continue
      height = df.at[x, "Heights"]
      n_height = height/max_height
      hbos = math.log10(1/n_height)
      #normalizing the bin height, and then finding the HBOS score for this bin
      p_hbos = df.at[x, "HBOS"]
      df.at[x, "HBOS"] = p_hbos + hbos
      #adding this HBOS score to the previous one


  df = df.drop(["Heights"], axis = 1)
  #dropping the heights column as it's only needed for the maths
  df = df.sort_values(by = "HBOS", ascending = False)
  df = df.reset_index(drop = True)
  #resorting the data so that it goes from the largest HBOS value to the smallest
  print(df)
  print("This is for the time interval " + timestamp)
  df.to_csv('HBOS_topten_fortime' + timestamp + '.csv')
  #outputting the data to a comma separated value sheet with an additional column for the HBOS scores
  #for further analysis