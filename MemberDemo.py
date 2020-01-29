import pandas as pd
import numpy as np
from pandas import Series,DataFrame
data = DataFrame(pd.read_excel('/Users/amy/Downloads/Member.xlsx'))
print(data)
#更改列名
data.rename(columns={0:'序号',1:'姓名',2:'年龄',3:'体重',4:'男三围1',5:'男三围2',6:'男三围3',7:'女三围1',8:'女三围2',9:'女三围3'},inplace = True)
#去掉重复行
data = data.drop_duplicates()
#1.完整性
#填充缺失值
col = data.columns.values.tolist()
row = data._stat_axis.values.tolist()
#先把姓名的数据类型改成字符串
data['姓名']=data['姓名'].astype('str')
#1.1先清除行
data.dropna(how = 'all',inplace = True)
#1.2 填充缺失值
age_maxf = data['年龄'].value_counts().index[0]
#以年龄频率最大值来填充
data['年龄'].fillna(age_maxf,inplace=True)
#2.全面性
#把体重单位为lbs的转化为kgs 2.2lbs = 1kgs
#把所有体重单位为lbs的记录存放在一起（如果体重是nan则不要）
rows_with_lbs = data['体重'].str.contains('lbs').fillna(False)
for i,lbs_row in data[rows_with_lbs].iterrows():
    weight = int(float(lbs_row['体重'][:-3])/2.2)
    #第一参数是y坐标（竖）第二个参数x坐标（横)
    data.at[i,'体重'] = '{}kgs'.format(weight)
    print (data)
#把清洗后的数据输出
data.to_excel('/Users/amy/Downloads/MemberCleanData2.xlsx')