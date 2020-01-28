import pandas as pd
df = pd.read_csv("/Users/amy/Downloads/food.csv")
df['food'].str.lower()
df.dropna(inplace=True)
df['ounces'] = df['ounces'].apply(lambda a:abs(a))
d_rows = df[df['food'].duplicated(keep=False)]
g_items = d_rows.groupby('food').mean()
g_items['food']=g_items.index
print (g_items)

for i,row in g_items.iterrows():
    df.loc[df.food == row.food,'ounces'] = row.ounces
    df.drop_duplicates(inplace=True)
    df.index = range(len(df))
    print(df)