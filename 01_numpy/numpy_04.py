import numpy as np 

a = np.array([1,2,3])

b = np.array([4,5,6])

x = np.concatenate((a,b))
y = np.stack((a,b), axis=1)
z = np.hstack((a,b))
xx = np.vstack((a,b))
yy = np.dstack((a,b))

print(x)
print(y)
print(z)
print(xx)
print(yy)

x = np.array_split(x, 2)
y = np.array_split(y,2)

print(x[0])
print(y)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)