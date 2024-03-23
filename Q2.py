import numpy as np

arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([2, 4, 6, 8])

print("Addition is: ",np.add(arr_1,arr_2))
print("Substraction is: ",np.subtract(arr_1,arr_2))
print("Multiplication is: ",np.multiply(arr_1,arr_2))
print("Division is: ",np.divide(arr_1,arr_2))

#part a
arr_3=np.random.randint(0,100, size=(3,4))
print(arr_3)

#part b
print("Logarithmic value of array 1:",np.log(arr_1))
print("Exponential value of array 1:",np.log(arr_2))

#part c
arr_4 = np.array([1.2, 2.5, 5.6, 3.4, 7.8])
print("Floor value of array 4: ",np.floor(arr_4))
print("Ceil value of array 4: ",np.ceil(arr_4))
