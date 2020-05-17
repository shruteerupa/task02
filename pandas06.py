import pandas as pd
df = pd.read_csv('C:/Users/shrutee/Downloads/diamonds.zip')
print("Original Dataframe:")
print(df.shape)
print("Sample 75% of diamonds DataFrame's rows without replacement:")
result = df.sample(frac=0.75, random_state=99)
print(result)
print("Remaining 25% of the rows:")
print(df.loc[~df.index.isin(result.index), :])