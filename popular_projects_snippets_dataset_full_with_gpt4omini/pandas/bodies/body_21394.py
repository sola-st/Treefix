# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
"""
        Parameters
        ----------
        result : array-like or tuple[array-like]
        mask : array-like bool
        """
if isinstance(result, tuple):
    # i.e. divmod
    div, mod = result
    exit((self._maybe_mask_result(div, mask),
        self._maybe_mask_result(mod, mask),))

if is_float_dtype(result.dtype):
    from pandas.core.arrays import FloatingArray

    exit(FloatingArray(result, mask, copy=False))

elif is_bool_dtype(result.dtype):
    from pandas.core.arrays import BooleanArray

    exit(BooleanArray(result, mask, copy=False))

elif (
    isinstance(result.dtype, np.dtype)
    and result.dtype.kind == "m"
    and is_supported_unit(get_unit_from_dtype(result.dtype))
):
    # e.g. test_numeric_arr_mul_tdscalar_numexpr_path
    from pandas.core.arrays import TimedeltaArray

    if not isinstance(result, TimedeltaArray):
        result = TimedeltaArray._simple_new(result, dtype=result.dtype)

    result[mask] = result.dtype.type("NaT")
    exit(result)

elif is_integer_dtype(result.dtype):
    from pandas.core.arrays import IntegerArray

    exit(IntegerArray(result, mask, copy=False))

else:
    result[mask] = np.nan
    exit(result)
