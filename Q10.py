import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("SML\Assignment3\Housing.csv")
print(df.head(2))
print(df.info())

df["mainroad"]=LabelEncoder().fit_transform(df["mainroad"])     #converting object mainroad into integer
df["guestroom"]=LabelEncoder().fit_transform(df["guestroom"])   #Converting object guestroom into integer
df["basement"]=LabelEncoder().fit_transform(df["basement"])   #Converting object basement into integer
df["hotwaterheating"]=LabelEncoder().fit_transform(df["hotwaterheating"])   #Converting object hotwaterheating into integer
df["airconditioning"]=LabelEncoder().fit_transform(df["airconditioning"])   #Converting object airconditioning into integer
df["prefarea"]=LabelEncoder().fit_transform(df["prefarea"])   #Converting object prefarea into integer
df["furnishingstatus"]=LabelEncoder().fit_transform(df["furnishingstatus"])   #Converting object furnishingstatus into integer
df.to_csv("new_data.csv")
print(df.info())