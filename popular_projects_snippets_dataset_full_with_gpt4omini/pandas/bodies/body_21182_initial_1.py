import numpy as np # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._parent = {1: MockColumn(), 2: MockColumn()}# pragma: no cover
class MockColumn:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.array = MockArray()# pragma: no cover
class MockArray:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.density = np.random.rand() # pragma: no cover

self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
from l3.Runtime import _l_
"""
        Ratio of non-sparse points to total (dense) data points.
        """
tmp = np.mean([column.array.density for _, column in self._parent.items()])
_l_(10124)
aux = tmp
_l_(10125)
exit(aux)
