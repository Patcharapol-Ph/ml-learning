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

a = np.array([1.1,2.2,3.3,4.4,5.5,6.6])
b = np.array([1,0,-1])

    a.astype("i") = [1,2,3,4,5,6]
    b.astype("b") = [True,False,True]

and also array can be copy using .copy()

a = np.array([1,2,3,4])
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

---

next is numpy_04 i just cramped all the remaining course in w3school
this is he results of my training:

array join can be dont in difference way like
concatenate will join the two array next to each other
Ex. x = np.array([1,2,3])
y = np.array([4,5,6])

    arr = np.concatenate(x,y)

    print(arr)
    result:
        [1,2,3,4,5,6]

stack which just like concatenate but can change the axis it join the array require an axis to tell the function which axis will be stacjing
Ex. arr = np.stack(x,y, axis=1)

    result:
        [[1,4],
            [2,5],
            [3,6]]

hstack and vstack work like stack but just state whih direction will be stacking
Ex. arr = np.hstack(x,y)
arr = np.vstack(x,y)

    result:
        [1,2,3,4,5,6]
        [[1,2,3],
            [4,5,6]]

dstack is stack with the depth of the array
Ex. x = 1 y = 4
2 5
3 6

    stack with depth result in [[1,4],[2,5],[3,6]]

next is spliting the argument to tell function how many array use want to split into doesn't need to mach the array because the function will adjust the array as the argument

Ex x = np.array([1,2,3,4,5,6])
x = x.array_split(x, 4)

    result:
        [array([1, 2]), array([3, 4]), array([5]), array([6])]

the split can be use in any array dimention can also add axis or use hsplit to get the same result if axis = 1
Ex. arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

    newarr = np.hsplit(arr, 3) or
    newarr = np.array_split(arr, 3, axis=1)

    result:
        [array([[ 1],
            [ 4],
            [ 7],
            [10],
            [13],
            [16]]), array([[ 2],
            [ 5],
            [ 8],
            [11],
            [14],
            [17]]), array([[ 3],
            [ 6],
            [ 9],
            [12],
            [15],
            [18]])]

now is array search have two way to search an Array
first is np.where will returen the position of Array can work in any dimentsion of array and can use function in the where
Ex. x = np.array([1,2,3,4,5])

    x = np.where(x == 3)

    result:
        [2]

    or use with and function

    x = np.where(x%2 == 0) //to find even number

    result:
        [1,3]

the other search is np.searchsorted use in and sort array because it iterlate the array to find which spot that the function get to add in array to make it sort
Ex. x = np.array9[1,2,3,4,5]

# this is to find the position where if add the number 6 to the array which position still make the array sort which is next to 5

    x = np.searchsorted(x,6)

the function can also add side to told the function which side to start form

- the side sometime effect the out put value of the function but does not effect the array because if default searchsorted will search from the left which will make it add value at the front but if the side is right it will place the value in the ack insted result in just 1 value difference

next is sort which will sort the smallest array can be work with any array dimension
Ex. arr = np.array([[6,9,8],[4,1,5]])

    x = np.sort(arr)

    result:
        [[6 8 9]
            [1 4 5]]

and lastly is array filter numpy can exclude the data from array if give boolean to the position
Ex. arr = np.array([41, 42, 43, 44])

    x = [True, False, True, False]

    newarr = arr[x]

    result:
        [41,43]

with this can be make to and function to filter the array like this w3school example
arr = np.array([41, 42, 43, 44])

# Create an empty list

filter_arr = []

# go through each element in arr

for element in arr:

# if the element is higher than 42, set the value to True, otherwise False:

if element > 42:
filter_arr.append(True)
else:
filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

but i tried to use this logic to work with the 2 dimentsion array but the problem is the filter_arr is and list and i don't know how to do that so i search online and found that it can just insert the function directly like this

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

arr = arr[arr%2 == 0]

result:
[2 4 6 8 10]

and that it!! i finish w3shcool numpy course the next part is i will be using this knowledge to create some mini project that focus on using numpy which of course the topic of project come from my dear friend ChatGPT
