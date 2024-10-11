import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import isna # pragma: no cover
import pandas.core.common as com # pragma: no cover

class MockGrouper:  # Mock class simulating grouper behavior# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 0, 1, 1]), None, 2)# pragma: no cover
    @property# pragma: no cover
    def result_index(self):# pragma: no cover
        return pd.Index(['Group 0', 'Group 1']) # pragma: no cover
class MockSelf:  # Mocking the main object# pragma: no cover
    def __init__(self):# pragma: no cover
        self.grouper = MockGrouper()# pragma: no cover
        self.as_index = True# pragma: no cover
        self.observed = False# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return pd.Series([1, 2, 3, 4])# pragma: no cover
    def _wrap_agged_manager(self, mgr):# pragma: no cover
        return mgr# pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.fillna(fill_value) # pragma: no cover
self = MockSelf() # pragma: no cover
data = self._get_data_to_aggregate() # pragma: no cover
ids, _, ngroups = self.grouper.group_info # pragma: no cover
mask = ids != -1 # pragma: no cover
is_series = data.ndim == 1 # pragma: no cover
data.grouped_reduce = lambda func: func(data.values) # pragma: no cover
com.temp_setattr = lambda obj, attr, value: setattr(obj, attr, value) # pragma: no cover

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
