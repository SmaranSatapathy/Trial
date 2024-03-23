import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris_data=sns.load_dataset('iris')  #loading the dataset named as IRIS
sns.pairplot(iris_data)
plt.savefig("Iris data graph plots.jpg")    #Saving the image of the graph plots
plt.show()
