from pandas import DataFrame # pragma: no cover

import pandas as pd # pragma: no cover

class DataManager:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
        self.axes = [pd.Index(data.index), pd.Index(data.columns)] # pragma: no cover
data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})# pragma: no cover
self = DataManager(data1) # pragma: no cover
data2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})# pragma: no cover
other = DataManager(data2) # pragma: no cover
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
