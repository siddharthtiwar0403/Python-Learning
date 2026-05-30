import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

#1D Array
arr = np.array([10, 20, 30])
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr[-1])
## In python negative indexing also exists which start with -1 from last last element of the array


## 2D Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr)


print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(np.zeros((3, 4)))
print(np.ones((2, 3)))
print(np.full((2,2), 9))
print(np.arange(1, 11))
print(np.linspace(0, 100, 4))
## In python negative indexing also exists which start with -1 from last row and last column of the array same goes with higher order arrays