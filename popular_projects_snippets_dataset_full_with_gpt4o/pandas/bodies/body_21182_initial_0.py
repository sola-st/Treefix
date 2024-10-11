import numpy as np # pragma: no cover

np = type('Mock', (object,), {'mean': lambda x: sum(x) / len(x)})() # pragma: no cover
self = type('Mock', (object,), {'_parent': {1: type('Mock', (object,), {'array': type('Mock', (object,), {'density': 0.75})()})(), 2: type('Mock', (object,), {'array': type('Mock', (object,), {'density': 0.85})()})()}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
from l3.Runtime import _l_
"""
        Ratio of non-sparse points to total (dense) data points.
        """
tmp = np.mean([column.array.density for _, column in self._parent.items()])
_l_(20877)
aux = tmp
_l_(20878)
exit(aux)
