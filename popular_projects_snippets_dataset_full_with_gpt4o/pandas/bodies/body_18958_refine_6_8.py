import numpy as np # pragma: no cover
from typing import Any, List # pragma: no cover
from pandas.api.types import is_object_dtype, is_integer_dtype # pragma: no cover
from pandas.core.arrays import ExtensionArray # pragma: no cover
from pandas.core.dtypes.cast import maybe_cast_to_integer_array # pragma: no cover
from pandas.core.construction import ensure_wrapped_if_datetimelike, construct_1d_object_array_from_listlike # pragma: no cover
from pandas import Index, Series # pragma: no cover

arr: List[Any] = [1, 2, 3, 4] # pragma: no cover
dtype: np.dtype = np.dtype('int') # pragma: no cover
copy: bool = True # pragma: no cover
class MockLib: ensure_string_array = lambda arr, convert_na_value, copy: np.array(arr, dtype='str') # pragma: no cover
lib = MockLib() # pragma: no cover
cast = lambda type_var, var: var # pragma: no cover
arr = type('MockArray', (np.ndarray,), {})((4,), buffer=np.array([1, 2, 3, 4])) # pragma: no cover

import numpy as np # pragma: no cover
from pandas.api.types import is_object_dtype, is_integer_dtype # pragma: no cover
from pandas.core.dtypes.cast import maybe_cast_to_integer_array # pragma: no cover
from pandas.core.construction import construct_1d_object_array_from_listlike, ensure_wrapped_if_datetimelike # pragma: no cover
from typing import cast # pragma: no cover

arr = np.array([1, 2, 3]) # pragma: no cover
dtype = np.dtype('int64') # pragma: no cover
copy = True # pragma: no cover
def construct_1d_object_array_from_listlike(arr): return np.array(arr, dtype=object) # pragma: no cover
def ensure_wrapped_if_datetimelike(arr): return arr # pragma: no cover
def maybe_cast_to_datetime(arr, dtype): return np.array(arr, dtype=dtype) # pragma: no cover
def maybe_cast_to_integer_array(arr, dtype): return np.array(arr, dtype=dtype) if np.issubdtype(arr.dtype, np.integer) else np.array(arr, dtype=dtype, casting='safe') # pragma: no cover
np.ndarray = np.array([1, 2, 3]).__class__ # pragma: no cover
arr.shape = (3,) # pragma: no cover
lib = type('Mock', (object,), {'ensure_string_array': lambda arr, convert_na_value, copy: np.array(arr, dtype=str)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/construction.py
from l3.Runtime import _l_
"""
    Convert input to numpy ndarray and optionally cast to a given dtype.

    Parameters
    ----------
    arr : ndarray or list
        Excludes: ExtensionArray, Series, Index.
    dtype : np.dtype
    copy : bool
        If False, don't copy the data if not needed.

    Returns
    -------
    np.ndarray or ExtensionArray
    """
is_ndarray = isinstance(arr, np.ndarray)
_l_(19522)

if is_object_dtype(dtype):
    _l_(19540)

    if not is_ndarray:
        _l_(19525)

        subarr = construct_1d_object_array_from_listlike(arr)
        _l_(19523)
        aux = subarr
        _l_(19524)
        exit(aux)
    aux = ensure_wrapped_if_datetimelike(arr).astype(dtype, copy=copy)
    _l_(19526)
    exit(aux)

elif dtype.kind == "U":
    _l_(19539)

    # TODO: test cases with arr.dtype.kind in ["m", "M"]
    if is_ndarray:
        _l_(19532)

        arr = cast(np.ndarray, arr)
        _l_(19527)
        shape = arr.shape
        _l_(19528)
        if arr.ndim > 1:
            _l_(19530)

            arr = arr.ravel()
            _l_(19529)
    else:
        shape = (len(arr),)
        _l_(19531)
    aux = lib.ensure_string_array(arr, convert_na_value=False, copy=copy).reshape(
        shape
    )
    _l_(19533)
    exit(aux)

elif dtype.kind in ["m", "M"]:
    _l_(19538)

    aux = maybe_cast_to_datetime(arr, dtype)
    _l_(19534)
    exit(aux)

# GH#15832: Check if we are requesting a numeric dtype and
# that we can convert the data to the requested dtype.
elif is_integer_dtype(dtype):
    _l_(19537)

    # this will raise if we have e.g. floats

    subarr = maybe_cast_to_integer_array(arr, dtype)
    _l_(19535)
else:
    subarr = np.array(arr, dtype=dtype, copy=copy)
    _l_(19536)
aux = subarr
_l_(19541)

exit(aux)
