import numpy as np # pragma: no cover
from pandas import Series, DataFrame, isna # pragma: no cover
import pandas as pd # pragma: no cover

self = type('Mock', (object,), {'_get_data_to_aggregate': lambda: np.array([1, 2, 3, 4, 5]), 'grouper': type('Grouper', (object,), {'group_info': (np.array([0, 0, 1, 1, 2]), None, 3)})() , 'as_index': True, '_wrap_agged_manager': lambda x: x, '_reindex_output': lambda x, fill_value: x})() # pragma: no cover
ids, _, ngroups = self.grouper.group_info # pragma: no cover
mask = ids != -1 # pragma: no cover

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
