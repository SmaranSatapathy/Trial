import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("SML\Assignment3\ComputerSales.csv")
print(df.isna().sum())

plt.scatter(df["Sale Price"],df["Profit"])
plt.xlabel("Sales Price")
plt.ylabel("Profit")
plt.show()