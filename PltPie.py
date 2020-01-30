import matplotlib.pyplot as plt
nums =[25,37,33,37,6]
labels = ['High-school','Bachelor','Master','Ph.d','others']
#Matplotlib画饼状图
plt.pie(x = nums, labels = labels)
plt.show()