import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#数据准备
a = np.random.randn(100)
s = pd.Series(a)
#用Matplotlib画直方图
plt.hist(s)
plt.show()
#用Seaborn画直方图
sns.displot(s,kde=False)
plt.show()
sns.displot(s,kde=True)
plt.show()

