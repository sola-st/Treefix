import numpy as np # pragma: no cover
from numpy import ndarray # pragma: no cover
from pandas import Series, Index # pragma: no cover
from pandas.api.extensions import ExtensionArray # pragma: no cover

arr = [1, 2, 3] # pragma: no cover
def is_object_dtype(dtype): return dtype.kind == 'O' # pragma: no cover
dtype = np.dtype('float64') # pragma: no cover
def construct_1d_object_array_from_listlike(arr): return np.array(arr, dtype=object) # pragma: no cover
def ensure_wrapped_if_datetimelike(arr): return arr # pragma: no cover
copy = True # pragma: no cover
cast = np.asarray # pragma: no cover
lib = type('Mock', (object,), {'ensure_string_array': staticmethod(lambda arr, convert_na_value: np.array(arr, dtype='<U10'))})() # pragma: no cover
def maybe_cast_to_datetime(arr, dtype): return np.array(arr, dtype=dtype) # pragma: no cover
def is_integer_dtype(dtype): return np.issubdtype(dtype, np.integer) # pragma: no cover
def maybe_cast_to_integer_array(arr, dtype): return np.array(arr, dtype=dtype) # pragma: no cover

import numpy as np # pragma: no cover
from numpy import ndarray # pragma: no cover
from pandas import Series, Index # pragma: no cover
from pandas.api.extensions import ExtensionArray # pragma: no cover

arr = np.array([1, 2, 3]) # pragma: no cover
def is_object_dtype(dtype): return dtype.kind == 'O' # pragma: no cover
dtype = np.dtype('float64') # pragma: no cover
def construct_1d_object_array_from_listlike(arr): return np.array(arr, dtype=object) # pragma: no cover
def ensure_wrapped_if_datetimelike(arr): return arr # pragma: no cover
copy = True # pragma: no cover
cast = np.asarray # pragma: no cover
lib = type('Mock', (object,), {'ensure_string_array': staticmethod(lambda arr, convert_na_value: np.array(arr, dtype='<U10'))})() # pragma: no cover
def maybe_cast_to_datetime(arr, dtype): return np.array(arr, dtype=dtype) # pragma: no cover
def is_integer_dtype(dtype): return np.issubdtype(dtype, np.integer) # pragma: no cover
def maybe_cast_to_integer_array(arr, dtype): return np.array(arr, dtype=dtype) # pragma: no cover

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
_l_(7088)

if is_object_dtype(dtype):
    _l_(7106)

    if not is_ndarray:
        _l_(7091)

        subarr = construct_1d_object_array_from_listlike(arr)
        _l_(7089)
        aux = subarr
        _l_(7090)
        exit(aux)
    aux = ensure_wrapped_if_datetimelike(arr).astype(dtype, copy=copy)
    _l_(7092)
    exit(aux)

elif dtype.kind == "U":
    _l_(7105)

    # TODO: test cases with arr.dtype.kind in ["m", "M"]
    if is_ndarray:
        _l_(7098)

        arr = cast(np.ndarray, arr)
        _l_(7093)
        shape = arr.shape
        _l_(7094)
        if arr.ndim > 1:
            _l_(7096)

            arr = arr.ravel()
            _l_(7095)
    else:
        shape = (len(arr),)
        _l_(7097)
    aux = lib.ensure_string_array(arr, convert_na_value=False, copy=copy).reshape(
        shape
    )
    _l_(7099)
    exit(aux)

elif dtype.kind in ["m", "M"]:
    _l_(7104)

    aux = maybe_cast_to_datetime(arr, dtype)
    _l_(7100)
    exit(aux)

# GH#15832: Check if we are requesting a numeric dtype and
# that we can convert the data to the requested dtype.
elif is_integer_dtype(dtype):
    _l_(7103)

    # this will raise if we have e.g. floats

    subarr = maybe_cast_to_integer_array(arr, dtype)
    _l_(7101)
else:
    subarr = np.array(arr, dtype=dtype, copy=copy)
    _l_(7102)
aux = subarr
_l_(7107)

exit(aux)
