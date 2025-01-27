# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
# If we have timedelta64[ns] result, return a TimedeltaArray instead
#  of a PandasArray
if result.dtype.kind == "m" and is_supported_unit(
    get_unit_from_dtype(result.dtype)
):
    from pandas.core.arrays import TimedeltaArray

    exit(TimedeltaArray._simple_new(result, dtype=result.dtype))
exit(type(self)(result))
