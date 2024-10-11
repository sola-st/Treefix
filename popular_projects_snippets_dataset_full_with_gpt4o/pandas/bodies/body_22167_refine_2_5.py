import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.api.extensions import ExtensionArray # pragma: no cover
from pandas.core.dtypes.missing import isna # pragma: no cover
from pandas.core.internals import BlockManager # pragma: no cover
import types # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
com = type('Mock', (object,), {})() # pragma: no cover
lib = type('Mock', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.sum(masked, axis=axis)})() # pragma: no cover
self._get_data_to_aggregate = lambda: pd.DataFrame({'a': [1, 2, np.nan, 4], 'b': [np.nan, 2, 3, 4]}) # pragma: no cover
self.grouper = type('Mock', (object,), {'group_info': (np.array([0, 0, -1, 1]), None, 2), 'result_index': pd.Index(['A', 'B'])})() # pragma: no cover
com.temp_setattr = lambda obj, attr, value: types.SimpleNamespace(**{attr: value}) # pragma: no cover
self._wrap_agged_manager = lambda mgr: pd.DataFrame({'a': [2, 1], 'b': [0, 2]}) # pragma: no cover
self.as_index = True # pragma: no cover
self._insert_inaxis_grouper = lambda result: result # pragma: no cover
self._reindex_output = lambda result, fill_value: result.fillna(fill_value) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import types # pragma: no cover

class MockGrouper:# pragma: no cover
    group_info = (np.array([0, 1, -1, 0, 1]), None, 2)# pragma: no cover
    result_index = pd.Index([0, 1]) # pragma: no cover
class MockDataFrame(pd.DataFrame):# pragma: no cover
    def grouped_reduce(self, func):# pragma: no cover
        return func(self.values) # pragma: no cover
class MockSelf:# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return MockDataFrame({'A': [1, 2, None, 4, 5], 'B': [None, 2, 3, None, 5]})# pragma: no cover
    def _wrap_agged_manager(self, mgr):# pragma: no cover
        return mgr# pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.fillna(fill_value) # pragma: no cover
self = MockSelf() # pragma: no cover
self.grouper = MockGrouper() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj, attr, value):# pragma: no cover
        original = getattr(obj, attr)# pragma: no cover
        setattr(obj, attr, value)# pragma: no cover
        yield# pragma: no cover
        setattr(obj, attr, original) # pragma: no cover
com = MockCom() # pragma: no cover
def lib_count_level_2d(masked, labels, max_bin, axis):# pragma: no cover
    group_counts = np.zeros(max_bin)# pragma: no cover
    for i, label in enumerate(labels):# pragma: no cover
        if masked[i]:# pragma: no cover
            group_counts[label] += 1# pragma: no cover
    return group_counts.reshape(1, -1) if axis == 1 else group_counts # pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lib_count_level_2d}) # pragma: no cover
self.as_index = True # pragma: no cover

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
_l_(21730)
ids, _, ngroups = self.grouper.group_info
_l_(21731)
mask = ids != -1
_l_(21732)

is_series = data.ndim == 1
_l_(21733)

def hfunc(bvalues: ArrayLike) -> ArrayLike:
    _l_(21743)

    # TODO(EA2D): reshape would not be necessary with 2D EAs
    if bvalues.ndim == 1:
        _l_(21736)

        # EA
        masked = mask & ~isna(bvalues).reshape(1, -1)
        _l_(21734)
    else:
        masked = mask & ~isna(bvalues)
        _l_(21735)

    counted = lib.count_level_2d(masked, labels=ids, max_bin=ngroups, axis=1)
    _l_(21737)
    if is_series:
        _l_(21741)

        assert counted.ndim == 2
        _l_(21738)
        assert counted.shape[0] == 1
        _l_(21739)
        aux = counted[0]
        _l_(21740)
        exit(aux)
    aux = counted
    _l_(21742)
    exit(aux)

new_mgr = data.grouped_reduce(hfunc)
_l_(21744)

# If we are grouping on categoricals we want unobserved categories to
# return zero, rather than the default of NaN which the reindexing in
# _wrap_agged_manager() returns. GH 35028
with com.temp_setattr(self, "observed", True):
    _l_(21746)

    result = self._wrap_agged_manager(new_mgr)
    _l_(21745)

if result.ndim == 1:
    _l_(21750)

    if self.as_index:
        _l_(21749)

        result.index = self.grouper.result_index
        _l_(21747)
    else:
        result = self._insert_inaxis_grouper(result)
        _l_(21748)
aux = self._reindex_output(result, fill_value=0)
_l_(21751)

exit(aux)
