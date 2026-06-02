import numpy as np

# ==================================================
# ARRAY CREATION
# ==================================================

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])

zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 3))
full_arr = np.full((2, 3), 7)
empty_arr = np.empty((2, 3))
arange_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

# ==================================================
# ATTRIBUTES
# ==================================================

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)

# ==================================================
# INDEXING
# ==================================================

arr1d = np.array([10, 20, 30, 40, 50])

print(arr1d[0])
print(arr1d[-1])

arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2d[0, 1])
print(arr2d[1, 2])

arr3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr3d[0, 1, 1])
print(arr3d[1, 0, 0])

# ==================================================
# SLICING
# ==================================================

print(arr1d[1:4])
print(arr1d[:3])
print(arr1d[::2])
print(arr1d[::-1])

print(arr2d[:, 1:])
print(arr2d[0:2, 0:2])

# ==================================================
# RESHAPING
# ==================================================

x = np.arange(1, 13)

reshaped = x.reshape(3, 4)
flattened = reshaped.flatten()
raveled = reshaped.ravel()
transposed = reshaped.T
transposed2 = np.transpose(reshaped)

# ==================================================
# ARITHMETIC OPERATIONS
# ==================================================

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a + 5)
print(a * 10)

# ==================================================
# BROADCASTING
# ==================================================

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)

# ==================================================
# COMPARISON OPERATORS
# ==================================================

a = np.array([10, 20, 30])

print(a == 20)
print(a != 20)
print(a > 15)
print(a < 25)
print(a >= 20)
print(a <= 20)

# ==================================================
# BOOLEAN MASKING
# ==================================================

a = np.array([10, 20, 30, 40, 50])

print(a[a > 25])
print(a[a % 2 == 0])

print(a[(a > 10) & (a < 50)])
print(a[(a < 20) | (a > 40)])

a[a > 30] = 999
print(a)

# ==================================================
# ITERATION
# ==================================================

a = np.array([10, 20, 30])

for x in a:
    print(x)

a = np.array([
    [1, 2],
    [3, 4]
])

for row in a:
    print(row)

for row in a:
    for element in row:
        print(element)

for x in np.nditer(a):
    print(x)

for index, value in enumerate(np.array([100, 200, 300])):
    print(index, value)

# ==================================================
# RANDOM MODULE
# ==================================================

np.random.seed(42)

print(np.random.rand())
print(np.random.rand(2, 3))

print(np.random.randn())
print(np.random.randn(2, 3))

print(np.random.randint(1, 10))
print(np.random.randint(1, 10, 5))
print(np.random.randint(1, 10, (2, 3)))

colors = ["red", "green", "blue"]
print(np.random.choice(colors))
print(np.random.choice(colors, 5))

# ==================================================
# SORTING & SEARCHING
# ==================================================

a = np.array([40, 10, 30, 20])

print(np.sort(a))
print(np.sort(a)[::-1])

print(np.argmax(a))
print(np.argmin(a))

print(np.where(a == 20))
print(np.where(a > 15))

print(np.argsort(a))

# ==================================================
# AGGREGATION FUNCTIONS
# ==================================================

a = np.array([10, 20, 30, 40])

print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))
print(np.var(a))

b = np.array([
    [1, 2],
    [3, 4]
])

print(np.sum(b, axis=0))
print(np.sum(b, axis=1))

# ==================================================
# ARRAY JOINING
# ==================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

print(np.hstack((a, b)))

print(np.vstack((a, b)))

print(np.stack((a, b)))
print(np.stack((a, b), axis=1))

# ==================================================
# ARRAY SPLITTING
# ==================================================

a = np.array([1, 2, 3, 4, 5, 6])

print(np.split(a, 3))

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(np.hsplit(a, 2))

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print(np.vsplit(a, 2))

# ==================================================
# LINEAR ALGEBRA
# ==================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(np.matmul(A, B))
print(A @ B) # @ is used for matrix multiplication in numpy

print(A.T)
print(np.transpose(A))

print(np.linalg.det(A))

print(np.linalg.inv(A))

print(np.random.randn(5))

c = np.array([1,2,3,4])
print(np.hsplit(c,2))

print(c[[0,1,3]]) ## this is called as fancy indexing which return multiple element from array withput using loop
