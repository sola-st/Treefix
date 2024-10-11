import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.api.extensions import ExtensionArray # pragma: no cover
from pandas import isna # pragma: no cover

class MockGrouper:# pragma: no cover
    @property# pragma: no cover
    def group_info(self):# pragma: no cover
        ids = np.array([0, 1, -1, 0, 1, 0])# pragma: no cover
        _, ngroups = np.unique(ids[ids != -1], return_inverse=True)# pragma: no cover
        return ids, None, len(np.unique(ngroups))# pragma: no cover
    # pragma: no cover
    @property# pragma: no cover
    def result_index(self):# pragma: no cover
        return pd.Index(['a', 'b']) # pragma: no cover
class MockSelf:# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return pd.DataFrame({'A': [1, 2, np.nan, 4, 5, 6]})# pragma: no cover
    # pragma: no cover
    grouper = MockGrouper()# pragma: no cover
    # pragma: no cover
    def _wrap_agged_manager(self, new_mgr):# pragma: no cover
        return new_mgr# pragma: no cover
    # pragma: no cover
    as_index = True# pragma: no cover
    # pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
    # pragma: no cover
    def _reindex_output(self, result, fill_value=0):# pragma: no cover
        return result.reindex(['a', 'b', 'c'], fill_value=fill_value) # pragma: no cover
self = MockSelf() # pragma: no cover
ArrayLike = ExtensionArray # pragma: no cover
com = type('MockCom', (object,), {'temp_setattr': lambda self, obj, name, value: (lambda: None)()})() # pragma: no cover
isna = pd.isna # pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.array([[np.sum(labels == i) for i in range(max_bin)]])})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 1, -1, 0, 1]), None, 2)# pragma: no cover
        self.result_index = pd.Index(['A', 'B'])# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def _get_data_to_aggregate(self):# pragma: no cover
        return MockDataFrame(np.array([[1, 2], [3, None], [None, 4], [5,6]]))# pragma: no cover
# pragma: no cover
    def _wrap_agged_manager(self, mgr):# pragma: no cover
        return mgr# pragma: no cover
# pragma: no cover
    def _insert_inaxis_grouper(self, result):# pragma: no cover
        return result# pragma: no cover
# pragma: no cover
    def _reindex_output(self, result, fill_value):# pragma: no cover
        return result.fillna(fill_value)# pragma: no cover
# pragma: no cover
    as_index = True# pragma: no cover
    grouper = MockGrouper()# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockDataFrame(pd.DataFrame):# pragma: no cover
    def grouped_reduce(self, func):# pragma: no cover
        return func(self.values)# pragma: no cover
# pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj, name, value):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                self.original = getattr(obj, name)# pragma: no cover
                setattr(obj, name, value)# pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
                setattr(obj, name, self.original)# pragma: no cover
        return ContextManager()# pragma: no cover
# pragma: no cover
com = MockCom() # pragma: no cover
lib = type('MockLib', (object,), {'count_level_2d': lambda masked, labels, max_bin, axis: np.array([[np.sum(labels == i) for i in range(max_bin)]])})() # pragma: no cover

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
