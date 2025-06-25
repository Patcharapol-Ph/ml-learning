# Numpy

in the first file numpy_intro.py

i learn about Creating Array and Other syntax

Syntax Learned:
first i import Numpy as np
import numpy as np

then np.array to create an Array
EX. np.array([1,2,3]) to get and array of [1,2,3]

which can be use more than one dimention and can controll dimentionwith
np.ndmin to set the array dimention
Ex. np.array([1,2,3,4], ndmin=5) to get [[[[[1,2,3,4]]]]]

in which the dimention of array can be confirm with syntax ndim
Ex. np.array([1,2,3], ndmin = 3).ndim to get 3 or
a = np.array([[1,2], [3,4]])
a.ndim to get 2

and type of these variable is numpy.ndarray
using type(np.array(0)) to get <class 'numpy.ndarray'>

and you can also check numpy version with np.(**version**)

---

in numpy_01 i learn about Array Indexing and Array Slicing

Array Indexing syntax is
arr[0], arr[0,1]
Ex. a = np.array([1,2,3,4,5])
b = np.array([[0,1,2],[3,4,5]])

a[0] = 1, a[3] = 4
b[0,2] = 2, b[1,0] = 3
which can also beuse in and caluclate method if it and number
a[2] + b[1,1] = 3 + 4 = 7

Array Slicing syntax is
arr[1:4], arr[::3]
arr[x:y] is that it will take value from x position till position before y
Ex. arr = np.array([1,2,3,4,5])
arr[1:4] = [2,3,4]
in which the syntax can also be leave empty and in an miunus value
if leave empty mean that it will use all of it
Ex. arr[:4] = [1,2,3,4]
arr[2:] = [3,4,5]
and if the value is minus it mean it will start from the end
Ex. arr[:-1] = [1,2,3,4]
arr[-1:] = [5]

and STEP which will determind which value will return from array
Ex. arr[::2] = [1,3,5]
which can also be use with slicing
Ex. arr[1:4:3] = [1,4]

---

in numpy_02 i learn about
type of data stored in array in which can be defined with syntax
dtype when initiated the array
Ex. a = np.array([1,2,3,4], dtype="i")

in which the type in dtype are
i: integer
b: boolean
u: unsigned integer
f: float
c: complex float
m: timedelta
M: datetime
O: object
S: string
U: unicode string
V: void

as the array can also beconvert after with syntax astype
Ex. a = np.array([1.1,2.2,3.3,4.4,5.5,6.6])
b = np.array([1,0,-1])

    a.astype("i") = [1,2,3,4,5,6]
    b.astype("b") = [True,False,True]

and also array can be copy using .copy()
Ex. a = np.array([1,2,3,4])
b = a.copy()

    b = [1,2,3,4]

---

in numpy_03 i learn about sharp of array and how to re shape
Ex. a = np.array([[1,2],[3,4],[5,6]])
a.shape() = (3,2)

and you can reshape Array with syntax reshape() but the array must match the reshapre
or else the function will return error
Ex a.reshape(2,3) = [[1,2,3],[4,5,6]]
a.reshape(2,4) = result in error because the Array not match the reshape

and how to iterate the array can be use with simple for loop
but can also beuse with nditer() in which can have and argument to use which range in array or use step
Ex. a = np.array([1,2,3,4,5,6])
for x in a:
print(a)

    result:
        1
        2
        3
        4
        5
        6

    for x in a.nditer()
        print(x)

will have the same resultbut nditer can be with arument such as
Ex. b = np.array([[1,2,3],[4,5,6]])
for x in b.nditer(:,::2)
print(x)

    result:
        1
        3
        4
        6
