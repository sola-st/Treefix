# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""wrap our results if needed"""
if result is NaT:
    pass

elif is_datetime64_any_dtype(dtype):
    if fill_value is None:
        # GH#24293
        fill_value = iNaT
    if not isinstance(result, np.ndarray):
        assert not isna(fill_value), "Expected non-null fill_value"
        if result == fill_value:
            result = np.nan

        if isna(result):
            result = np.datetime64("NaT", "ns").astype(dtype)
        else:
            result = np.int64(result).view(dtype)
        # retain original unit
        result = result.astype(dtype, copy=False)
    else:
        # If we have float dtype, taking a view will give the wrong result
        result = result.astype(dtype)
elif is_timedelta64_dtype(dtype):
    if not isinstance(result, np.ndarray):
        if result == fill_value or np.isnan(result):
            result = np.timedelta64("NaT").astype(dtype)

        elif np.fabs(result) > lib.i8max:
            # raise if we have a timedelta64[ns] which is too large
            raise ValueError("overflow in timedelta operation")
        else:
            # return a timedelta64 with the original unit
            result = np.int64(result).astype(dtype, copy=False)

    else:
        result = result.astype("m8[ns]").view(dtype)

exit(result)
