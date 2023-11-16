
import pandas as pd
import matplotlib.pyplot as plt

# Reading the data
df = pd.read_csv('test.csv')

# Short (initial) Visualization
print(df.head())
print('---------------------------')

# Descriptive Statistics
st_value = df['Value'].describe()
print(st_value)
print('---------------------------')


category_summary = df.groupby('Category')['Value'].agg(['mean', 'sum']).reset_index()
print(category_summary)
print('---------------------------')

