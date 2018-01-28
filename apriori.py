# Apriori

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transcations = []
for i in range(0, 7501):
    transcations.append([str(dataset.values[i,j]) for j in range(0,20)])