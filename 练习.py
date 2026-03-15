import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'D:\edge\titanic.csv')
print(df.head())
ages=df['Age'].dropna()
plt.hist(ages)
plt.title("分析数据")
plt.xlabel("年龄")
plt.ylabel("人数")
plt.show()
print("均值：",df['Age'].mean())
