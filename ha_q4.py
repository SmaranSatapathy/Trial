import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv",index_col="cars")

df["carname"]=LabelEncoder().fit_transform(df["carname"]) 
correlation_matrix=df.corr()
sns.heatmap(data=correlation_matrix,annot=True)
plt.show()