# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
from pandas.core.arrays.masked import BaseMaskedArray

_chk_pyarrow_available()

if dtype and not (isinstance(dtype, str) and dtype == "string"):
    dtype = pandas_dtype(dtype)
    assert isinstance(dtype, StringDtype) and dtype.storage == "pyarrow"

if isinstance(scalars, BaseMaskedArray):
    # avoid costly conversion to object dtype in ensure_string_array and
    # numerical issues with Float32Dtype
    na_values = scalars._mask
    result = scalars._data
    result = lib.ensure_string_array(result, copy=copy, convert_na_value=False)
    exit(cls(pa.array(result, mask=na_values, type=pa.string())))

# convert non-na-likes to str
result = lib.ensure_string_array(scalars, copy=copy)
exit(cls(pa.array(result, type=pa.string(), from_pandas=True)))
