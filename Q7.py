import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("ComputerSales.csv")
print(df.isna().sum())
print(df.info())
print(df.shape)
print(df.describe())

plt.subplot(2,3,1)
plt.hist(df["Sale ID"],edgecolor="black")

plt.subplot(2,3,2)
plt.hist(df["Age"])

plt.subplot(2,3,3)
plt.hist(df["Sale Price"])

plt.subplot(2,3,4)
plt.hist(df["Profit"])

plt.subplot(2,3,5)
plt.hist(df["Year"])

plt.suptitle("Histogram Graphs")
plt.tight_layout()
plt.show()