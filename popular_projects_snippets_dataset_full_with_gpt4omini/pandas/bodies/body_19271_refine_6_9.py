import pandas as pd # pragma: no cover
from pandas.core.dtypes.dtypes import ExtensionDtype, IntervalDtype # pragma: no cover

arr_or_dtype = pd.IntervalIndex([pd.Interval(1, 2)]) # pragma: no cover
class MockExtensionDtype(ExtensionDtype): pass # pragma: no cover
ExtensionDtype = MockExtensionDtype() # pragma: no cover
Interval = pd.Interval(1, 2) # pragma: no cover

import pandas as pd # pragma: no cover
from pandas.core.dtypes.dtypes import ExtensionDtype, IntervalDtype # pragma: no cover

arr_or_dtype = pd.IntervalIndex([pd.Interval(1, 2)]) # pragma: no cover
class MockExtensionDtype(ExtensionDtype): pass # pragma: no cover
ExtensionDtype = type('MockExtensionDtype', (ExtensionDtype,), {}) # pragma: no cover
Interval = pd.Interval(1, 2) # pragma: no cover
class MockIntervalDtype:  # pragma: no cover
    @staticmethod # pragma: no cover
    def is_dtype(value): # pragma: no cover
        return isinstance(value, (pd.Interval, pd.IntervalIndex)) # pragma: no cover
IntervalDtype = type('MockIntervalDtype', (object,), {'is_dtype': staticmethod(MockIntervalDtype.is_dtype)})() # pragma: no cover

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
    _l_(4552)

    aux = arr_or_dtype.type is Interval
    _l_(4551)
    # GH#33400 fastpath for dtype object
    exit(aux)

if arr_or_dtype is None:
    _l_(4554)

    aux = False
    _l_(4553)
    exit(aux)
aux = IntervalDtype.is_dtype(arr_or_dtype)
_l_(4555)
exit(aux)
