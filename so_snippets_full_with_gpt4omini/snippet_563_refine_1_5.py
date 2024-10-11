import numpy # pragma: no cover

import numpy # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
from l3.Runtime import _l_
x = numpy.fromfile(file=open("data"), dtype=float).reshape((100, 100, 100))
_l_(576)

s = x.sum(axis=1)
_l_(577)

(x > 0.5).nonzero()
_l_(578)

x[:, :, ::2]
_l_(579)

