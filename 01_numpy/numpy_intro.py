import numpy as np

print(np.__version__)

arr = np.array(42)

a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
d = np.array([1,2,3,4,5], ndmin=5)

print("0D Array:", arr)
print("1D Array:", a)
print("2D Array:", b)
print("3D Array:", c)
print("5D Array:", d)

print("arr Type:",type(arr))
print("a Type:",type(a))
print("b Type:",type(b))
print("c Type:",type(c))
print("d Type:",type(d))

print("arr Dimensional:", arr.ndim)
print("a Dimensional:",a.ndim)
print("b Dimensional:",b.ndim)
print("c Dimensional:",c.ndim)
print("d Dimensional:",d.ndim)