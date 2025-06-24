import numpy as np

arr = np.array([1,2,3,4,5,6,7])
a = np.array([[1,2,3,4],[3,4,5,6]])
b = np.array([[[1,3],[2,4]],[[1,2],[3,4]]])

print(arr[2] + arr[3])
print(a[0,1] + b[0,1,1])

print(arr[:4])
print(arr[-2:])
print(arr[::2])

print(a[1, 1:4])
print(a[:-1, ::2])