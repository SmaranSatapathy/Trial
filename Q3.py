import numpy as np
import matplotlib.pyplot as plt

arr_1=np.array(np.linspace(-np.pi,np.pi,200))
print(arr_1)
sin_value=np.sin(arr_1)
cos_value=np.cos(arr_1)
tan_value=np.tan(arr_1)

plt.subplot(1,3,1)
plt.plot(sin_value)
plt.xlabel("Values between -pi to pi")
plt.ylabel("Sine values")

plt.subplot(1,3,2)
plt.plot(cos_value)
plt.xlabel("Values between -pi to pi")
plt.ylabel("Cosine Values")

plt.subplot(1,3,3)
plt.plot(tan_value)
plt.xlabel("Values between -pi to pi")
plt.ylabel("Tangent values")

plt.tight_layout()
plt.show()