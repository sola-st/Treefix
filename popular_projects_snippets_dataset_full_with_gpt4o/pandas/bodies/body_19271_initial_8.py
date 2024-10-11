import pandas as pd # pragma: no cover
from pandas.api.extensions import ExtensionDtype # pragma: no cover

arr_or_dtype = object # pragma: no cover
class MockExtensionDtype(ExtensionDtype):# pragma: no cover
    @property# pragma: no cover
    def type(self):# pragma: no cover
        return Interval# pragma: no cover
arr_or_dtype = MockExtensionDtype() # pragma: no cover
class MockInterval:# pragma: no cover
    pass# pragma: no cover
Interval = MockInterval # pragma: no cover
class MockIntervalDtypeMock:# pragma: no cover
    @staticmethod# pragma: no cover
    def is_dtype(dtype):# pragma: no cover
        return isinstance(dtype, MockIntervalDtype)# pragma: no cover
interval_dtype_instance = MockIntervalDtypeMock()# pragma: no cover
IntervalDtype = type('IntervalDtype', (object,), {'is_dtype': interval_dtype_instance.is_dtype}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
from l3.Runtime import _l_
"""
    Check whether an array-like or dtype is of the Interval dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the Interval dtype.

    Examples
    --------
    >>> is_interval_dtype(object)
    False
    >>> is_interval_dtype(IntervalDtype())
    True
    >>> is_interval_dtype([1, 2, 3])
    False
    >>>
    >>> interval = pd.Interval(1, 2, closed="right")
    >>> is_interval_dtype(interval)
    False
    >>> is_interval_dtype(pd.IntervalIndex([interval]))
    True
    """
if isinstance(arr_or_dtype, ExtensionDtype):
    _l_(15948)

    aux = arr_or_dtype.type is Interval
    _l_(15947)
    # GH#33400 fastpath for dtype object
    exit(aux)

if arr_or_dtype is None:
    _l_(15950)

    aux = False
    _l_(15949)
    exit(aux)
aux = IntervalDtype.is_dtype(arr_or_dtype)
_l_(15951)
exit(aux)
