import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
print(df.info())
print(df.shape)

new_col=df.groupby("class").size()
print(new_col)

plt.pie(new_col,labels=new_col.index)
plt.show()