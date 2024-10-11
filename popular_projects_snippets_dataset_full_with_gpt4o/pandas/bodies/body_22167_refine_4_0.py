import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

self = type('Mock', (object,), {# pragma: no cover
    '_get_data_to_aggregate': lambda self: pd.DataFrame(np.random.randn(100, 3)),# pragma: no cover
    'grouper': type('MockGrouper', (object,), {'group_info': (np.random.randint(0, 5, size=100), None, 5), 'result_index': pd.Index(range(5))})(),# pragma: no cover
    '_wrap_agged_manager': lambda self, x: x,# pragma: no cover
    '_insert_inaxis_grouper': lambda self, x: x,# pragma: no cover
    '_reindex_output': lambda self, x, fill_value: x# pragma: no cover
})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
com = type('MockCom', (object,), {'temp_setattr': lambda self, obj, attr, value: (setattr(obj, attr, value), obj)})() # pragma: no cover
isna = pd.isna # pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.sum(masked, axis=0)})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockSelf:# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return MockDataFrame()# pragma: no cover
    def _wrap_agged_manager(self, mgr):# pragma: no cover
        return mgr# pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.fillna(fill_value)# pragma: no cover
# pragma: no cover
class MockGrouper:# pragma: no cover
    group_info = (np.array([0, 1, -1, 0, 1]), None, 2)# pragma: no cover
    result_index = pd.Index([0, 1])# pragma: no cover
# pragma: no cover
class MockDataFrame(pd.DataFrame):# pragma: no cover
    def grouped_reduce(self, func):# pragma: no cover
        return func(self.values)# pragma: no cover
# pragma: no cover
com = type('MockCom', (object,), {'temp_setattr': lambda self, obj, attr, value: (setattr(obj, attr, value), obj)})()# pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.bincount(labels[masked])})()# pragma: no cover
isna = pd.isna# pragma: no cover
ArrayLike = np.ndarray# pragma: no cover
self = MockSelf()# pragma: no cover
self.grouper = MockGrouper()# pragma: no cover
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
