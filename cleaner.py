import pandas as pd

df = pd.read_csv('final.csv', index_col=0)
print(df.shape)

del df['Star_Luminosity']

print(df.shape)
df.to_csv('main.csv')