import numpy as np

a = np.array([1,2,3,4], dtype="S")
b = np.array(["Apple", "Bannana","Orange"])
c = np.array([1.2,2.3,4.6])
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)
c = c.astype('i')

print(a.dtype)
print(b.dtype)
print(newarr)
print(c.dtype)
print(c)