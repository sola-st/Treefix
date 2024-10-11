import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from typing import Any, Tuple # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 1, -1, 0]), None, 2)# pragma: no cover
        self.result_index = pd.Index(['A', 'B']) # pragma: no cover
class MockLib:# pragma: no cover
    @staticmethod# pragma: no cover
    def count_level_2d(masked, labels, max_bin, axis):# pragma: no cover
        return np.array([[np.sum(masked[labels == i]) for i in range(max_bin)]]) # pragma: no cover
class MockCommon:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(instance, attr, value):# pragma: no cover
        original = getattr(instance, attr)# pragma: no cover
        setattr(instance, attr, value)# pragma: no cover
        return original # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.grouper = MockGrouper()# pragma: no cover
        self.as_index = False# pragma: no cover
        self._get_data_to_aggregate = lambda: pd.Series([1, 2, np.nan, 4])# pragma: no cover
        self._wrap_agged_manager = lambda x: x# pragma: no cover
        self._insert_inaxis_grouper = lambda x: x# pragma: no cover
        self._reindex_output = lambda x, fill_value: x.fillna(fill_value) # pragma: no cover
self = MockSelf() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
isna = pd.isna # pragma: no cover
lib = MockLib() # pragma: no cover
com = MockCommon() # pragma: no cover

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
