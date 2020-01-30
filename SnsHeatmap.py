import matplotlib.pyplot as plt
import seaborn as sns
flights = sns.load_dataset("flights")
data = flights.pivot('year','month','passengers')
#用Seaborn画热力图
sns.heatmap(data)
plt.show()