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

#getting the data from the sheet, I think
df = pd.read_csv("LCCC_munged_Dec18_system_memory1.csv")

# Import model
from pyod.models.hbos import HBOS
df.index.get_level_values('system_memory_actual_used_bytes')
df.plot.scatter('system_memory_actual_used_bytes','system_memory_used_bytes')
