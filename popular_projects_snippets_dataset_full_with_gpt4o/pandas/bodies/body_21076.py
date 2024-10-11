# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
if dtype and not (isinstance(dtype, str) and dtype == "string"):
    dtype = pandas_dtype(dtype)
    assert isinstance(dtype, StringDtype) and dtype.storage == "python"

from pandas.core.arrays.masked import BaseMaskedArray

if isinstance(scalars, BaseMaskedArray):
    # avoid costly conversion to object dtype
    na_values = scalars._mask
    result = scalars._data
    result = lib.ensure_string_array(result, copy=copy, convert_na_value=False)
    result[na_values] = libmissing.NA

else:
    # convert non-na-likes to str, and nan-likes to StringDtype().na_value
    result = lib.ensure_string_array(scalars, na_value=libmissing.NA, copy=copy)

# Manually creating new array avoids the validation step in the __init__, so is
# faster. Refactor need for validation?
new_string_array = cls.__new__(cls)
NDArrayBacked.__init__(new_string_array, result, StringDtype(storage="python"))

exit(new_string_array)
