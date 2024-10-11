import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import isna # pragma: no cover

class MockDataManager: # pragma: no cover
    def grouped_reduce(self, func): # pragma: no cover
        # dummy 2D data assuming 3 groups for testing purposes # pragma: no cover
        data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) # pragma: no cover
        return func(data) # pragma: no cover
 # pragma: no cover
class MockGrouper: # pragma: no cover
    group_info = (np.array([0, 1, 1, -1, 2, 2]), None, 3) # pragma: no cover
    result_index = pd.Index(['a', 'b', 'c']) # pragma: no cover
 # pragma: no cover
class MockCom: # pragma: no cover
    @staticmethod # pragma: no cover
    def temp_setattr(instance, attribute, value): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                setattr(instance, attribute, value) # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                pass # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
class MockLib: # pragma: no cover
    @staticmethod # pragma: no cover
    def count_level_2d(masked, labels, max_bin, axis): # pragma: no cover
        # returns dummy counts assuming 3 groups for 2D input data # pragma: no cover
        return np.array([[3, 2, 1]]) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_get_data_to_aggregate': lambda self: MockDataManager(), # pragma: no cover
    'grouper': MockGrouper(), # pragma: no cover
    '_wrap_agged_manager': lambda self, mgr: mgr, # pragma: no cover
    'as_index': True, # pragma: no cover
    '_insert_inaxis_grouper': lambda self, result: result, # pragma: no cover
    '_reindex_output': lambda self, result, fill_value: result # pragma: no cover
})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
com = MockCom() # pragma: no cover
lib = MockLib() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import isna # pragma: no cover

class MockDataManager:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
        self.ndim = data.ndim# pragma: no cover
    def grouped_reduce(self, func):# pragma: no cover
        return func(self.data) # pragma: no cover
class MockGrouper:# pragma: no cover
    group_info = (np.array([0, 1, 1, -1, 2, 2]), None, 3)# pragma: no cover
    result_index = pd.Index(['a', 'b', 'c']) # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(instance, attribute, value):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                self.original = getattr(instance, attribute)# pragma: no cover
                setattr(instance, attribute, value)# pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
                setattr(instance, attribute, self.original)# pragma: no cover
        return ContextManager() # pragma: no cover
class MockLib:# pragma: no cover
    @staticmethod# pragma: no cover
    def count_level_2d(masked, labels, max_bin, axis):# pragma: no cover
        # returns dummy counts assuming 3 groups for 2D input data# pragma: no cover
        return np.array([[3, 2, 1]]) # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_get_data_to_aggregate': lambda self: MockDataManager(np.random.randn(6, 5)), # pragma: no cover
    'grouper': MockGrouper(), # pragma: no cover
    '_wrap_agged_manager': lambda self, mgr: mgr, # pragma: no cover
    'as_index': True, # pragma: no cover
    '_insert_inaxis_grouper': lambda self, result: result, # pragma: no cover
    '_reindex_output': lambda self, result, fill_value: result.fillna(fill_value) # pragma: no cover
})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
com = MockCom() # pragma: no cover
lib = MockLib() # pragma: no cover

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
