import pandas  as pd
import numpy as np
df = pd.read_csv("/Users/amy/Downloads/food.csv")
#去掉列名空格，否则影响后续对列的操作
df.columns =df.columns.str.strip()
#去掉food列名称空格，否则影响对名称的操作
df['food'] = df['food'].str.strip()
#对food名称首字母大写
df['food'] = df['food'].str.capitalize()
#对ounces列负值取绝对值
df['ounces'] = df['ounces'].apply(lambda a:abs(a))
#在取绝对值后用列平均值填充NaN值
df.fillna(df.mean(),inplace=True)
#删除food列重复数据
df.drop_duplicates('food',inplace=True)
df.to_csv("/Users/amy/Downloads/foodclean.csv")
print(df)