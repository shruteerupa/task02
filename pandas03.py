import pandas as pd
df= pd.read_csv('C:/Users/shrutee/Downloads/diamonds.zip')
print("\nCount, minimum, maximum  price for each cut of diamonds DataFrame:")
print(df.groupby('cut').price.agg(['count', 'min', 'max']))