"""This is the script for DPhi Course.
Challenge: Electronics Products Pricing
Data Sprint #16
"""

import pandas as pd
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.utils import resample
# from imblearn.over_sampling import SMOTE
#
# matplotlib.use('Qt5Agg')
pd.set_option('display.max_columns', 25)
pd.set_option('display.width', 1000)
train = pd.read_csv('Training_set_label.csv')
# EDA
print(train.shape)
print(train.head())
print(train.dtypes)
print(train.info())
print(train.describe(include='all'))

# Data treatment
missing_values = (train.isnull().sum())
print(missing_values[missing_values > 0])
print(missing_values[missing_values > 0] / train.shape[0] * 100)

# print(train['Sex'].value_counts())
# print(train['Sex'].unique())
# print(train['Sex'].value_counts(normalize=True) * 100)
