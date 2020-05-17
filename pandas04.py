import pandas as pd
df = pd.read_csv('C:/Users/shrutee/Downloads/diamonds.zip')
print("Original Dataframe:")
print(df.head())
print("Number of rows and columns:")
print(df.shape)
print("After droping those rows where values are missing:")
print(df.dropna(how='any').shape)