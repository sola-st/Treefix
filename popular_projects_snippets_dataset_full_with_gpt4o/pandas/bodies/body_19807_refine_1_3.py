import pandas as pd # pragma: no cover
from pandas.testing import assert_frame_equal # pragma: no cover

class DataManager:# pragma: no cover
    def __init__(self, axes, values=None):# pragma: no cover
        self.axes = axes# pragma: no cover
        self.values = values if values is not None else []# pragma: no cover
    def equality_check(self, other):# pragma: no cover
        try:# pragma: no cover
            for ax_self, ax_other in zip(self.axes, other.axes):# pragma: no cover
                assert_frame_equal(ax_self, ax_other)# pragma: no cover
            return True# pragma: no cover
        except AssertionError:# pragma: no cover
            return False# pragma: no cover
    def _equal_values(self, other):# pragma: no cover
        return self.equality_check(other) # pragma: no cover
other = DataManager([pd.DataFrame({'a': [1, 2, 3]}), pd.DataFrame({'b': [4, 5, 6]})]) # pragma: no cover
self = DataManager([pd.DataFrame({'a': [1, 2, 3]}), pd.DataFrame({'b': [4, 5, 6]})]) # pragma: no cover

import pandas as pd # pragma: no cover

class DataManager:# pragma: no cover
    def __init__(self, df):# pragma: no cover
        self.df = df# pragma: no cover
        self.axes = [df.index, df.columns]# pragma: no cover
    def _equal_values(self, other):# pragma: no cover
        return self.df.equals(other.df) # pragma: no cover
data = {'col1': [1, 2], 'col2': [3, 4]} # pragma: no cover
self = DataManager(pd.DataFrame(data)) # pragma: no cover
other = DataManager(pd.DataFrame(data)) # pragma: no cover

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
