import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
print(df)



    
print(df.isna().sum())
count=df["manufacturer"].value_counts()
plt.bar(df["manufacturer"].unique(),count,color="red")
plt.xlabel("Manufacturer")
plt.ylabel("Number of cars")
plt.tight_layout()
plt.show()