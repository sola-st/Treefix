import numpy as np # pragma: no cover

a = np.array([[1, 2, 3], [4, 5, 6]]) # pragma: no cover
numpy = np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape
from l3.Runtime import _l_
b = numpy.reshape(a, -1)
_l_(4065)

