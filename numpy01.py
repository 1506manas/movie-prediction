import numpy as np
import sys

l = range(1000)
print(sys.getsizeof(1)*len(l))

a = np.arange(1000)
print(array.itemsize*len(a))
