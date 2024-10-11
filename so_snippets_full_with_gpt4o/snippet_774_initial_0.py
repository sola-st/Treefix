import numpy as np # pragma: no cover

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # pragma: no cover
numpy = np # pragma: no cover
R = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22053050/difference-between-numpy-array-shape-r-1-and-r
from l3.Runtime import _l_
np.outer(M[:,0], numpy.ones((1, R)))
_l_(13173)

