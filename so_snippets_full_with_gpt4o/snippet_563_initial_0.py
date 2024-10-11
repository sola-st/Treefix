import numpy as np # pragma: no cover

numpy = type('Mock', (object,), {'fromfile': lambda file, dtype: np.random.rand(1000000)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
from l3.Runtime import _l_
x = numpy.fromfile(file=open("data"), dtype=float).reshape((100, 100, 100))
_l_(12459)

s = x.sum(axis=1)
_l_(12460)

(x > 0.5).nonzero()
_l_(12461)

x[:, :, ::2]
_l_(12462)

