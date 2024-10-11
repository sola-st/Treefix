import numpy as np # pragma: no cover
from typing import Any # pragma: no cover
from pandas import Series, DataFrame # pragma: no cover

class MockLib:# pragma: no cover
    @staticmethod# pragma: no cover
    def count_level_2d(masked: Any, labels: Any, max_bin: int, axis: int) -> np.ndarray:# pragma: no cover
        return np.random.randint(1, 10, size=(max_bin, 1 if axis == 1 else masked.shape[axis]))# pragma: no cover
# pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj: Any, name: str, value: Any):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                self.original_value = getattr(obj, name)# pragma: no cover
                setattr(obj, name, value)# pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
                setattr(obj, name, self.original_value)# pragma: no cover
        return ContextManager()# pragma: no cover
# pragma: no cover
def isna(array: Any) -> np.ndarray:# pragma: no cover
    return np.isnan(array)# pragma: no cover
# pragma: no cover
ArrayLike = np.ndarray# pragma: no cover
# pragma: no cover
class MockGrouper:# pragma: no cover
    def __init__(self, ngroups: int):# pragma: no cover
        self.group_info = (np.random.randint(0, ngroups, size=100), None, ngroups)# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, data: ArrayLike, ngroups: int):# pragma: no cover
        self.data = data# pragma: no cover
        self.grouper = MockGrouper(ngroups)# pragma: no cover
        self.as_index = True# pragma: no cover
    def _get_data_to_aggregate(self) -> ArrayLike:# pragma: no cover
        return self.data# pragma: no cover
    def _wrap_agged_manager(self, new_mgr: ArrayLike) -> DataFrame:# pragma: no cover
        return DataFrame(new_mgr)# pragma: no cover
    def _insert_inaxis_grouper(self, result: ArrayLike) -> Series:# pragma: no cover
        return Series(result)# pragma: no cover
    def _reindex_output(self, result: Any, fill_value: int) -> Any:# pragma: no cover
        return result.reindex(range(10), fill_value=fill_value)# pragma: no cover
# pragma: no cover
self = MockSelf(data=np.random.randn(100, 4), ngroups=5)# pragma: no cover
lib = MockLib()# pragma: no cover
com = MockCom() # pragma: no cover

import numpy as np # pragma: no cover
from typing import Any # pragma: no cover
from pandas import Series, DataFrame # pragma: no cover

class MockLib:# pragma: no cover
    @staticmethod# pragma: no cover
    def count_level_2d(masked: Any, labels: Any, max_bin: int, axis: int) -> np.ndarray:# pragma: no cover
        return np.random.randint(1, 10, size=(max_bin, 1 if axis == 1 else masked.shape[axis]))# pragma: no cover
# pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj: Any, name: str, value: Any):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                self.original_value = getattr(obj, name)# pragma: no cover
                setattr(obj, name, value)# pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
                setattr(obj, name, self.original_value)# pragma: no cover
        return ContextManager()# pragma: no cover
# pragma: no cover
def isna(array: Any) -> np.ndarray:# pragma: no cover
    return np.isnan(array)# pragma: no cover
# pragma: no cover
ArrayLike = np.ndarray# pragma: no cover
# pragma: no cover
class MockData:# pragma: no cover
    def __init__(self, data: ArrayLike):# pragma: no cover
        self.data = data# pragma: no cover
    def grouped_reduce(self, func: Any) -> ArrayLike:# pragma: no cover
        return func(self.data)# pragma: no cover
# pragma: no cover
class MockGrouper:# pragma: no cover
    def __init__(self, ngroups: int):# pragma: no cover
        self.group_info = (np.random.randint(0, ngroups, size=100), None, ngroups)# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, data: ArrayLike, ngroups: int):# pragma: no cover
        self.data = MockData(data)# pragma: no cover
        self.grouper = MockGrouper(ngroups)# pragma: no cover
        self.as_index = True# pragma: no cover
    def _get_data_to_aggregate(self) -> ArrayLike:# pragma: no cover
        return self.data# pragma: no cover
    def _wrap_agged_manager(self, new_mgr: ArrayLike) -> DataFrame:# pragma: no cover
        return DataFrame(new_mgr)# pragma: no cover
    def _insert_inaxis_grouper(self, result: ArrayLike) -> Series:# pragma: no cover
        return Series(result)# pragma: no cover
    def _reindex_output(self, result: Any, fill_value: int) -> Any:# pragma: no cover
        return result.reindex(range(10), fill_value=fill_value)# pragma: no cover
# pragma: no cover
self = MockSelf(data=np.random.randn(100, 4), ngroups=5)# pragma: no cover
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
