import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/gauraviiita/Supervised_ML/main/Datasets/Chapter_2/police.csv")

print(df.isna().sum())


mean_values=df["driver_age_raw"].mean()
df["driver_age_raw"]=df["driver_age_raw"].fillna(mean_values)
print("Post edit->")
print(df.isna().sum())