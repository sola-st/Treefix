import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class DataManager:# pragma: no cover
    def __init__(self, axes):# pragma: no cover
        self.axes = axes# pragma: no cover
    # pragma: no cover
    def equals(self, other):# pragma: no cover
        return isinstance(other, DataManager) and all(ax1.equals(ax2) for ax1, ax2 in zip(self.axes, other.axes)) # pragma: no cover
self = type('Mock', (object,), {'axes': [pd.Index([1, 2, 3]), pd.Index([4, 5, 6])], '_equal_values': lambda self, other: np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3]))})() # pragma: no cover
other = DataManager([pd.Index([1, 2, 3]), pd.Index([4, 5, 6])]) # pragma: no cover

import pandas as pd # pragma: no cover

class DataManager: # pragma: no cover
    def __init__(self, axes): # pragma: no cover
        self.axes = axes # pragma: no cover
 # pragma: no cover
    def _equal_values(self, other): # pragma: no cover
        # Mock implementation of _equal_values # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
class MockAxis: # pragma: no cover
    def __init__(self, values): # pragma: no cover
        self.values = values # pragma: no cover
 # pragma: no cover
    def equals(self, other): # pragma: no cover
        return self.values.equals(other.values) # pragma: no cover
 # pragma: no cover
mock_ax1 = MockAxis(pd.Index([1, 2, 3])) # pragma: no cover
mock_ax2 = MockAxis(pd.Index([4, 5, 6])) # pragma: no cover
 # pragma: no cover
self = DataManager(axes=[mock_ax1, mock_ax2]) # pragma: no cover
other = DataManager(axes=[mock_ax1, mock_ax2]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
from l3.Runtime import _l_
"""
        Implementation for DataFrame.equals
        """
if not isinstance(other, DataManager):
    _l_(22251)

    aux = False
    _l_(22250)
    exit(aux)

self_axes, other_axes = self.axes, other.axes
_l_(22252)
if len(self_axes) != len(other_axes):
    _l_(22254)

    aux = False
    _l_(22253)
    exit(aux)
if not all(ax1.equals(ax2) for ax1, ax2 in zip(self_axes, other_axes)):
    _l_(22256)

    aux = False
    _l_(22255)
    exit(aux)
aux = self._equal_values(other)
_l_(22257)

exit(aux)
