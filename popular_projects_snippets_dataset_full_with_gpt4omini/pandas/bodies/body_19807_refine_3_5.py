import pandas as pd # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.axes = [pd.Index([1, 2, 3]), pd.Index(['a', 'b', 'c'])] # pragma: no cover
other = Mock() # pragma: no cover
other.axes = [pd.Index([1, 2, 3]), pd.Index(['a', 'b', 'c'])] # pragma: no cover
self._equal_values = lambda other: True # pragma: no cover
DataManager = Mock # pragma: no cover

import pandas as pd # pragma: no cover

class DataManager:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
        self.axes = [pd.Index(range(len(data))), pd.Index(data.columns)] # pragma: no cover
data_1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}# pragma: no cover
self = DataManager(pd.DataFrame(data_1)) # pragma: no cover
data_2 = {'A': [1, 2, 3], 'B': [4, 5, 6]}# pragma: no cover
other = DataManager(pd.DataFrame(data_2)) # pragma: no cover
def _equal_values(self, other):# pragma: no cover
    return self.data.equals(other.data)# pragma: no cover
self._equal_values = _equal_values.__get__(self) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
from l3.Runtime import _l_
"""
        Implementation for DataFrame.equals
        """
if not isinstance(other, DataManager):
    _l_(10715)

    aux = False
    _l_(10714)
    exit(aux)

self_axes, other_axes = self.axes, other.axes
_l_(10716)
if len(self_axes) != len(other_axes):
    _l_(10718)

    aux = False
    _l_(10717)
    exit(aux)
if not all(ax1.equals(ax2) for ax1, ax2 in zip(self_axes, other_axes)):
    _l_(10720)

    aux = False
    _l_(10719)
    exit(aux)
aux = self._equal_values(other)
_l_(10721)

exit(aux)
