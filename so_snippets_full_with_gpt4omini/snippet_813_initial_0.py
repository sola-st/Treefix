import numpy as np # pragma: no cover

c = np.array([[1, 2, 3], [4, 5, 6]]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1966207/convert-numpy-array-to-python-list
from l3.Runtime import _l_
c.ravel()
_l_(384)
# or
c.ravel().tolist()
_l_(385)

