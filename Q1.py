import pandas as pd

df=pd.read_csv("data.csv")
print(df.head()) #returns pehla 5 rows
print(df.shape)  #returns the rows n columns
print(df.isna().sum())  #returns total missing values from each columns

#1) Filling the missing values via mean
mean_value=df["Calories"].mean()
print(mean_value)
df["Calories"]=df["Calories"].fillna(mean_value)
print(df.isna().sum())

#2 Dropping the data
df.dropna(inplace=True)
print(df.isna().sum())

#Setting the dates format
df["Date"]=pd.to_datetime(df["Date"],format="mixed")    #format("Mixed") is  necesary attribute=>
print(df)

#Checking for values over 60s and changing it
for i in df.index:
    if(df.loc[i,"Duration"] >60):
        df.loc[i,"Duration"]=60
print(df)

#Dropping duplicates
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape)
print(df)

print(df.iloc[5:15,:])
