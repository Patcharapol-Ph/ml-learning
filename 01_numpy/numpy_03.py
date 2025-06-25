import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
arr = arr.reshape(2,2,2,2)

print(arr)

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

print("---")

for x in np.nditer(arr[::,:,::3]):
    print(x)

for idx, x in np.ndenumerate(arr):
    print(idx, x)