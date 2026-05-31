import numpy as np

# ==========================================
# ARRAY CREATION FUNCTIONS
# ==========================================

arr1 = np.array([1, 2, 3, 4, 5])
print("np.array():")
print(arr1)

arr2 = np.zeros((2, 3))
print("\nnp.zeros():")
print(arr2)

arr3 = np.ones((2, 3))
print("\nnp.ones():")
print(arr3)

arr4 = np.full((2, 3), 7)
print("\nnp.full():")
print(arr4)

arr5 = np.empty((2, 3))
print("\nnp.empty():")
print(arr5)

arr6 = np.arange(1, 11)
print("\nnp.arange():")
print(arr6)

arr7 = np.linspace(0, 100, 5)
print("\nnp.linspace():")
print(arr7)

# ==========================================
# ARRAY ATTRIBUTES
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nArray Attributes:")
print("ndim =", arr.ndim)
print("shape =", arr.shape)
print("size =", arr.size)
print("dtype =", arr.dtype)
print("itemsize =", arr.itemsize)

# ==========================================
# 1D INDEXING
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

print("\n1D Indexing:")
print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[-2])

# ==========================================
# 2D INDEXING
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Indexing:")
print(arr[0, 0])
print(arr[1, 2])
print(arr[-1, -1])
print(arr[-2, -2])

# ==========================================
# 3D INDEXING
# ==========================================

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Indexing:")
print(arr[0, 1, 1])
print(arr[1, 0, 1])
print(arr[-1, -1, -1])

# ==========================================
# 1D SLICING
# ==========================================

arr = np.array([10, 20, 30, 40, 50, 60])

print("\n1D Slicing:")
print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[:])
print(arr[::2])
print(arr[::-1])

# ==========================================
# 2D SLICING
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Slicing:")
print(arr[0, :])        # First row
print(arr[-1, :])       # Last row
print(arr[:, 0])        # First column
print(arr[:, -1])       # Last column
print(arr[0:2, 0:2])    # Top-left 2x2 matrix
print(arr[:, ::-1])     # Reverse columns
print(arr[::-1, :])     # Reverse rows

# ==========================================
# RESHAPE
# ==========================================

arr = np.array([1, 2, 3, 4, 5, 6])

print("\nreshape():")
print(arr.reshape(2, 3))
print(arr.reshape(3, 2))
print(arr.reshape(2, -1))

# ==========================================
# FLATTEN
# ==========================================

arr = np.array([
    [1, 2],
    [3, 4]
])

print("\nflatten():")
print(arr.flatten())

# ==========================================
# RAVEL
# ==========================================

print("\nravel():")
print(arr.ravel())

# ==========================================
# TRANSPOSE
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\ntranspose():")
print(arr.transpose())

print("\nTranspose Shortcut (.T):")
print(arr.T)