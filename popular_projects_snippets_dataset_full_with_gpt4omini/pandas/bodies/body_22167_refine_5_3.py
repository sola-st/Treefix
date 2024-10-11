import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import isna # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 1, 1, 0]), None, 2)# pragma: no cover
        self.result_index = np.array(['group_0', 'group_1'])# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.grouper = MockGrouper()# pragma: no cover
        self.as_index = True# pragma: no cover
        self.data = pd.Series([1,2,3,np.nan,4])# pragma: no cover
    # pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return self.data# pragma: no cover
    # pragma: no cover
    def _wrap_agged_manager(self, new_mgr):# pragma: no cover
        return new_mgr# pragma: no cover
    # pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    # pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.reindex(self.grouper.result_index, fill_value=fill_value)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
lib.count_level_2d = lambda masked, labels, max_bin, axis: np.sum(masked, axis=axis, keepdims=True) # pragma: no cover
com.temp_setattr = lambda obj, attr, value: setattr(obj, attr, value) # Mock implementation # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 1, 1, 0]), None, 2)# pragma: no cover
        self.result_index = pd.Index(['group_0', 'group_1'])# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.grouper = MockGrouper()# pragma: no cover
        self.as_index = True# pragma: no cover
        self.data = pd.Series([1, 2, 3, np.nan, 4])# pragma: no cover
    # pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return self.data# pragma: no cover
    # pragma: no cover
    def _wrap_agged_manager(self, new_mgr):# pragma: no cover
        return new_mgr# pragma: no cover
    # pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    # pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.reindex(self.grouper.result_index, fill_value=fill_value)# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
def count_level_2d(masked, labels, max_bin, axis):# pragma: no cover
    return np.array([[np.sum(masked[labels == i]) for i in range(max_bin)]])# pragma: no cover
# pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': staticmethod(count_level_2d)})() # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(instance, attr, value):# pragma: no cover
        original = getattr(instance, attr)# pragma: no cover
        setattr(instance, attr, value)# pragma: no cover
        return original# pragma: no cover
com = MockCom() # pragma: no cover
isna = pd.isna # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
from l3.Runtime import _l_
"""
        Compute count of group, excluding missing values.

        Returns
        -------
        Series or DataFrame
            Count of values within each group.
        """
data = self._get_data_to_aggregate()
_l_(10463)
ids, _, ngroups = self.grouper.group_info
_l_(10464)
mask = ids != -1
_l_(10465)

is_series = data.ndim == 1
_l_(10466)

def hfunc(bvalues: ArrayLike) -> ArrayLike:
    _l_(10476)

    # TODO(EA2D): reshape would not be necessary with 2D EAs
    if bvalues.ndim == 1:
        _l_(10469)

        # EA
        masked = mask & ~isna(bvalues).reshape(1, -1)
        _l_(10467)
    else:
        masked = mask & ~isna(bvalues)
        _l_(10468)

    counted = lib.count_level_2d(masked, labels=ids, max_bin=ngroups, axis=1)
    _l_(10470)
    if is_series:
        _l_(10474)

        assert counted.ndim == 2
        _l_(10471)
        assert counted.shape[0] == 1
        _l_(10472)
        aux = counted[0]
        _l_(10473)
        exit(aux)
    aux = counted
    _l_(10475)
    exit(aux)

new_mgr = data.grouped_reduce(hfunc)
_l_(10477)

# If we are grouping on categoricals we want unobserved categories to
# return zero, rather than the default of NaN which the reindexing in
# _wrap_agged_manager() returns. GH 35028
with com.temp_setattr(self, "observed", True):
    _l_(10479)

    result = self._wrap_agged_manager(new_mgr)
    _l_(10478)

if result.ndim == 1:
    _l_(10483)

    if self.as_index:
        _l_(10482)

        result.index = self.grouper.result_index
        _l_(10480)
    else:
        result = self._insert_inaxis_grouper(result)
        _l_(10481)
aux = self._reindex_output(result, fill_value=0)
_l_(10484)

exit(aux)
