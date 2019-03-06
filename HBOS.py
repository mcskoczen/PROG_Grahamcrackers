# Author: Yue Zhao <yuezhao@cs.toronto.edu>
# License: BSD 2 clause
# ignore this line

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
df = pd.read_csv("LCCC_munged_Dec18_system_memory.csv")

# Import model
from pyod.models.hbos import HBOS

# Define the number of inliers and outliers
n_samples = 200
outliers_fraction = 0.25
clusters_separation = [0]

# Compare given detectors under given settings
# Initialize the data
xx, yy = np.meshgrid(np.linspace(0, 7, 100), np.linspace(0, 7, 100))
n_inliers = int((1. - outliers_fraction) * n_samples)
n_outliers = int(outliers_fraction * n_samples)
ground_truth = np.zeros(n_samples, dtype=int)
ground_truth[-n_outliers:] = 1

# Show the statics of the data
print('Number of inliers: %i' % n_inliers)
print('Number of outliers: %i' % n_outliers)
print(
  'Ground truth shape is {shape}. Outlier are 1 and inliers are 0.\n'.format(
      shape=ground_truth.shape))
print(ground_truth, '\n')

# Define the outlier detection tool(s) used
classifiers = {
  'Histogram-base Outlier Detection (HBOS)': HBOS(
      contamination=outliers_fraction),
}

# Show all detectors
for i, clf in enumerate(classifiers.keys()):
  print('Model', i + 1, clf)

# Fit the model(s) with the generated data and
# compare model performances
for i, offset in enumerate(clusters_separation):
  np.random.seed(42)
  # Data generation
  X1 = 0.3 * np.random.randn(n_inliers // 2, 2) + offset
  X2 = 0.3 * np.random.randn(n_inliers // 2, 2) + offset
  X = np.r_[X1, X2]
  # Add outliers
  X = np.r_[X, np.random.uniform(low=0, high=7, size=(n_outliers, 2))]

  # Fit the model
  plt.figure(figsize=(15, 12))
  for i, (clf_name, clf) in enumerate(classifiers.items()):
      print()
      print(i + 1, 'fitting', clf_name)
      # fit the data and tag outliers
      clf.fit(X)
      scores_pred = clf.decision_function(X) * -1
      y_pred = clf.predict(X)
      threshold = stats.scoreatpercentile(scores_pred,
                                          100 * outliers_fraction)
      n_errors = (y_pred != ground_truth).sum()
      # plot the levels lines and the points

      Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]) * -1
      Z = Z.reshape(xx.shape)
      subplot = plt.subplot(3, 4, i + 1)

      #decides the colors for the plot
      subplot.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7), cmap=plt.cm.Greys_r)
      a = subplot.contour(xx, yy, Z, levels=[threshold],
                          linewidths=2, colors='blue')
      subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                       colors='orange')
      b = subplot.scatter(X[:-n_outliers, 0], X[:-n_outliers, 1], c='red',
                          s=20, edgecolor='k')
      c = subplot.scatter(X[-n_outliers:, 0], X[-n_outliers:, 1], c='green',
                          s=20, edgecolor='k')
      subplot.axis('tight')
      subplot.set_xlabel("%d. %s (errors: %d)" % (i + 1, clf_name, n_errors))
      subplot.set_xlim((0, 7))
      subplot.set_ylim((0, 7))
  plt.subplots_adjust(0.04, 0.1, 0.96, 0.94, 0.1, 0.26)
  plt.suptitle("Outlier detection")
plt.savefig('ALL.png', dpi=300)
plt.show()
