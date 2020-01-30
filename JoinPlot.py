import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.head(10))
sns.jointplot(x="total_bill",y="tip",data=tips,kind='scatter')
sns.jointplot(x="total_bill",y="tip",data=tips,kind='kde')
sns.jointplot(x="total_bill",y="tip",data=tips,kind='hex')
plt.show()
