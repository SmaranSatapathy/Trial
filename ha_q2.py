import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv")
print(df)

plt.plot(df["date"],df["value"],  color="orange")
plt.xlabel("Date of takeoff")
plt.ylabel("Passengers")
plt.title("Flight Details from 1949 to 1959")
plt.show()