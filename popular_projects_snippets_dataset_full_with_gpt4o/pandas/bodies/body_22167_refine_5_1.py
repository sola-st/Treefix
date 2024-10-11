import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.core.dtypes.missing import isna # pragma: no cover
import pandas._libs.lib as lib # pragma: no cover
import types # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, 1, -1, 0]), None, 2)# pragma: no cover
        self.result_index = pd.Index(['A', 'B'])# pragma: no cover
# pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
    '_get_data_to_aggregate': lambda self: pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, 6, 7, 8]}),# pragma: no cover
    'grouper': MockGrouper(),# pragma: no cover
    'as_index': True,# pragma: no cover
    '_wrap_agged_manager': lambda self, mgr: mgr,# pragma: no cover
    '_insert_inaxis_grouper': lambda self, result: result,# pragma: no cover
    '_reindex_output': lambda self, result, fill_value: result.fillna(fill_value)# pragma: no cover
})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    def temp_setattr(obj, attr, value):# pragma: no cover
        original = getattr(obj, attr)# pragma: no cover
        setattr(obj, attr, value)# pragma: no cover
        try:# pragma: no cover
            yield# pragma: no cover
        finally:# pragma: no cover
            setattr(obj, attr, original)# pragma: no cover
# pragma: no cover
com = MockCom# pragma: no cover
# pragma: no cover
MockCom.temp_setattr = contextlib.contextmanager(MockCom.temp_setattr) # pragma: no cover
 # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.core.dtypes.missing import isna # pragma: no cover
import pandas._libs.lib as lib # pragma: no cover
import contextlib # pragma: no cover

class MockGrouper:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.group_info = (np.array([0, -1, 1, 0]), None, 2)# pragma: no cover
        self.result_index = pd.Index(['A', 'B'])# pragma: no cover
# pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
    '_get_data_to_aggregate': lambda self: pd.DataFrame({'A': [1, np.nan, 3, 4], 'B': [10, 20, 30, 40]}),# pragma: no cover
    'grouper': MockGrouper(),# pragma: no cover
    'as_index': True,# pragma: no cover
    '_wrap_agged_manager': lambda self, mgr: mgr,# pragma: no cover
    '_insert_inaxis_grouper': lambda self, result: result,# pragma: no cover
    '_reindex_output': lambda self, result, fill_value: result.fillna(fill_value)# pragma: no cover
})() # pragma: no cover
ArrayLike = np.ndarray # pragma: no cover
class MockCom:# pragma: no cover
    @staticmethod# pragma: no cover
    @contextlib.contextmanager# pragma: no cover
    def temp_setattr(obj, attr, value):# pragma: no cover
        original = getattr(obj, attr)# pragma: no cover
        setattr(obj, attr, value)# pragma: no cover
        try:# pragma: no cover
            yield# pragma: no cover
        finally:# pragma: no cover
            setattr(obj, attr, original)# pragma: no cover
# pragma: no cover
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
