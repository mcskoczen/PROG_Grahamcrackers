import csv
with open('LCCC_munged_Dec18_system_memory1.csv', newline= '') as memory:
  reader = csv.reader(memory)
  for row in reader:
    print(row)
    
#defining the class for the computer as the outer bit for each
class computer:
  def __init__(self, branch, host):
        self.branch = branch
        self.host = host

class timestamp(computer):
  def __init__(self, timestamp):
    self.timestamp = timestamp
    pass

class mem(timestamp):
  def __init__(self, actual, swap, total):
    pass