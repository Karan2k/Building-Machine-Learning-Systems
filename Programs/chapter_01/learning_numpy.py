import numpy as np

# prints the version of numpy
print np.version.full_version

a = np.array([0, 1, 2, 3, 4, 5])
# prints the dimensional count of array a
print a.ndim

# prints the dimensions of array a
print a.shape

# generates a 2D matrix with dimension 3 x 2
b = a.reshape((3, 2))
print b

# prints 2
print b.ndim

# prints (3, 2)
print b.shape