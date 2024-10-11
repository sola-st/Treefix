import pandas as pd # pragma: no cover

DataManager = type('DataManager', (object,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'axes': [pd.Index([1, 2, 3]), pd.Index([4, 5, 6])], '_equal_values': lambda self, other: True})() # pragma: no cover

DataManager = type('DataManager', (object,), {}) # pragma: no cover
class MockAxis:# pragma: no cover
    def equals(self, other):# pragma: no cover
        return True # pragma: no cover
self = type('MockSelf', (object,), {'axes': [MockAxis(), MockAxis()], '_equal_values': lambda self, other: True})() # pragma: no cover
other = type('MockOther', (DataManager,), {'axes': [MockAxis(), MockAxis()]})() # pragma: no cover

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
