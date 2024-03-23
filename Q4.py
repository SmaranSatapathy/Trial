import numpy as np
from numpy import linalg as LA

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[2, 4], [6, 9]])

dot_product=np.dot(arr_1,arr_2)
print("Dot product is: ",dot_product)

eigen_values,eigen_vectors=LA.eig(arr_1)
print("Eigen values are: ",eigen_values)
print("Eigen vectors are: ",eigen_vectors)

determinant1=LA.det(arr_1)
print("Determinant of arr 1 is: ",determinant1)

determinant2=LA.det(arr_2)
print("Determinant of arr 2 is: ",determinant2)

inv1=LA.inv(arr_1)
print("Inverse of array  1 is: ",inv1)

inv2=LA.inv(arr_2)
print("Inverse of array 2 is: ",inv2)
