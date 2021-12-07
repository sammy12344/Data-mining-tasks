import numpy as np
from numpy import random

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Inserting values at random positions
rows, cols = np.shape(arr)
positions = max(rows, cols)
while positions > 0:
    arr[np.random.choice(rows), np.random.choice(cols)] = 0
    positions = positions - 1
print(arr)

# Row-wise sums
row_sums = arr.sum(axis=1)
arr = np.insert(arr, cols, values=row_sums, axis=1)

# Column-wise sums
col_sums = arr.sum(axis=0)
arr = np.vstack([arr, col_sums])

print(arr)
