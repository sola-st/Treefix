# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
dtype = pandas_dtype(dtype)
if is_dtype_equal(dtype, np.dtype("timedelta64")):
    # no precision disallowed GH#24806
    msg = (
        "Passing in 'timedelta' dtype with no precision is not allowed. "
        "Please pass in 'timedelta64[ns]' instead."
    )
    raise ValueError(msg)

if (
    not isinstance(dtype, np.dtype)
    or dtype.kind != "m"
    or not is_supported_unit(get_unit_from_dtype(dtype))
):
    raise ValueError(f"dtype {dtype} cannot be converted to timedelta64[ns]")

exit(dtype)
