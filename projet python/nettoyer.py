import pandas as pd
import numpy as np
import re


data = pd.read.csv('personnes.csv')
print(data)

print(data.isnull().sum())