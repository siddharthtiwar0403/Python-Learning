import numpy as np

X = np.random.rand(1000000, 100)

print("Shape:", X.shape)
print("Size:", X.size)
print("Item Size:", X.itemsize)
print("Bytes:", X.nbytes)
print("MB:", X.nbytes / (1024**2))
