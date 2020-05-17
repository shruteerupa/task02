import pandas as pd
df = pd.read_csv('C:/Users/shrutee/Downloads/diamonds.zip')
print("Original Dataframe:")
print(df.shape)
print("Duplicate rows of diamonds DataFrame:")
print(df.duplicated().sum())