import numpy as np # pragma: no cover

self = type('Mock', (object,), {'_parent': {'col1': type('ColumnMock', (object,), {'array': type('ArrayMock', (object,), {'density': 0.6})()})(), 'col2': type('ColumnMock', (object,), {'array': type('ArrayMock', (object,), {'density': 0.8})()})()}})() # pragma: no cover

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
