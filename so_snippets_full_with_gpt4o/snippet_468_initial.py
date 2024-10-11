# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/35215161/most-efficient-way-to-map-function-over-numpy-array
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(14804)

except ImportError:
    pass
x = np.array([1, 2, 3, 4, 5])
_l_(14805)
squarer = lambda t: t ** 2
_l_(14806)
vfunc = np.vectorize(squarer)
_l_(14807)
vfunc(x)
_l_(14808)
# Output : array([ 1,  4,  9, 16, 25])

