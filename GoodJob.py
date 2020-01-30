#思考题1：对车祸数据成对关系的的探索，程序代码如下：

# 车祸数据分析
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 数据准备
crashes = sns.load_dataset('car_crashes')
crashes_data = pd.DataFrame(crashes)

# 用 Seaborn 画成对关系
sns.pairplot(crashes)
plt.show()

#思考题2：模拟企业隐患数据分析，代码如下：

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# 定义生成隐患数量函数
def GenerateHDNum(hdtimes):
    # hdtimes表示要生成多少隐患数量
    HD_NumList = list(pd.Series(np.random.rand(hdtimes)))
    return [int(x * 100) for x in HD_NumList]


# 数据准备函数
def MakeData():
    # 创建以月份为单位的时间索引
    dti = pd.date_range(start='2017-01-01', end='2018-12-31', freq='M')
    monthlist = [str(x * 100 + y) for x, y in zip(dti.year, dti.month)]

    hdtimes = len(monthlist)
    # 生成各种隐患数量
    NormalHD = GenerateHDNum(hdtimes)
    ImportHD = GenerateHDNum(hdtimes)
    HDNum = {'Normal': NormalHD
        , 'Import': ImportHD}

    HD_Frame = pd.DataFrame(data=HDNum, index=monthlist)

    print(HD_Frame)
    return HD_Frame


def AnalyData(HDSet, AnalyType='0'):
    # AnalyType取值：1：成对关系图；2：散点图；3：核密度图；4：Hexbin图

    # 成对关系图
    if AnalyType == '1':
        sns.pairplot(HDSet)

    # 散点图
    if AnalyType == '2':
        sns.jointplot(x='Normal', y='Import', data=HDSet, kind='scatter')

    # 核密度图
    if AnalyType == '3':
        sns.jointplot(x='Normal', y='Import', data=HDSet, kind='kde')

    # Hexbin图
    if AnalyType == '4':
        sns.jointplot(x='Normal', y='Import', data=HDSet, kind='hex')

    plt.show()


def ShowMenu():
    print('=' * 20)
    print('1.显示成对关系图')
    print('2.显示散点图')
    print('3.显示核密度图')
    print('4.显示Hexbin图')
    print('R.换一批数据')
    print('0.退出')
    print('=' * 20)
    return input('请输入命令:')


def main():
    HDSet = MakeData()
    while True:
        command = ShowMenu()

        if command == '0':
            break
        elif command == 'R':
            HDSet = MakeData()
        else:
            AnalyData(HDSet, command)


main()