#Numpy
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
