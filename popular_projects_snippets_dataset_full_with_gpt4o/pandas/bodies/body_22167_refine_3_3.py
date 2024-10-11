import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

self = type('Mock', (object,), {'_get_data_to_aggregate': lambda self: pd.DataFrame({'values': [1, None, 3, 4]}), 'grouper': type('MockGrouper', (object,), {'group_info': (np.array([0, -1, 1, 1]), None, 2), 'result_index': pd.Index(['A', 'B'])}), '_wrap_agged_manager': lambda self, mgr: mgr, '_insert_inaxis_grouper': lambda self, res: res, '_reindex_output': lambda self, result, fill_value: result})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
com = type('Mock', (object,), {'temp_setattr': lambda self, target, attr, value: (setattr(target, attr, value) or (yield))})() # pragma: no cover
isna = pd.isna # pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.bincount(labels[masked])})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockLib:# pragma: no cover
    @staticmethod# pragma: no cover
    def count_level_2d(masked, labels, max_bin, axis):# pragma: no cover
        group_counts = np.zeros((max_bin, 2)) if axis == 1 else np.zeros(max_bin)# pragma: no cover
        for i, label in enumerate(labels):# pragma: no cover
            if masked[i]:# pragma: no cover
                group_counts[label] += 1# pragma: no cover
        return group_counts if axis == 1 else group_counts.reshape(-1, 1)# pragma: no cover
# pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj, name, value):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                self.original_value = getattr(obj, name)# pragma: no cover
                setattr(obj, name, value)# pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
                setattr(obj, name, self.original_value)# pragma: no cover
        return ContextManager()# pragma: no cover
# pragma: no cover
ArrayLike = np.ndarray# pragma: no cover
# pragma: no cover
class MockGrouper:# pragma: no cover
    def __init__(self, ngroups):# pragma: no cover
        self.group_info = (np.array([0, 1, -1, 0, 1]), None, ngroups)# pragma: no cover
        self.result_index = pd.Index([0, 1])# pragma: no cover
# pragma: no cover
class MockData:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
    def grouped_reduce(self, func):# pragma: no cover
        return func(self.data.to_numpy())# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, data, ngroups):# pragma: no cover
        self.data = MockData(data)# pragma: no cover
        self.grouper = MockGrouper(ngroups)# pragma: no cover
        self.as_index = True# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return self.data# pragma: no cover
    def _wrap_agged_manager(self, new_mgr):# pragma: no cover
        return pd.DataFrame(new_mgr)# pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.reindex(range(10), fill_value=fill_value)# pragma: no cover
# pragma: no cover
self = MockSelf(pd.DataFrame({'a': [1, 2, np.nan, 4], 'b': [np.nan, 2, 3, 4]}), ngroups=2)# pragma: no cover
lib = MockLib()# pragma: no cover
com = MockCom() # pragma: no cover

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
