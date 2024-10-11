# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    Convert data based on dtype conventions, issuing
    errors where appropriate.

    Parameters
    ----------
    data : np.ndarray or pd.Index
    copy : bool
    tz : tzinfo or None, default None

    Returns
    -------
    data : np.ndarray or pd.Index
    copy : bool

    Raises
    ------
    TypeError : PeriodDType data is passed
    """
if not hasattr(data, "dtype"):
    # e.g. collections.deque
    exit((data, copy))

if is_float_dtype(data.dtype):
    # pre-2.0 we treated these as wall-times, inconsistent with ints
    # GH#23675, GH#45573 deprecated to treat symmetrically with integer dtypes.
    # Note: data.astype(np.int64) fails ARM tests, see
    # https://github.com/pandas-dev/pandas/issues/49468.
    data = data.astype("M8[ns]").view("i8")
    copy = False

elif is_timedelta64_dtype(data.dtype) or is_bool_dtype(data.dtype):
    # GH#29794 enforcing deprecation introduced in GH#23539
    raise TypeError(f"dtype {data.dtype} cannot be converted to datetime64[ns]")
elif is_period_dtype(data.dtype):
    # Note: without explicitly raising here, PeriodIndex
    #  test_setops.test_join_does_not_recur fails
    raise TypeError(
        "Passing PeriodDtype data is invalid. Use `data.to_timestamp()` instead"
    )

elif is_extension_array_dtype(data.dtype) and not is_datetime64tz_dtype(data.dtype):
    # TODO: We have no tests for these
    data = np.array(data, dtype=np.object_)
    copy = False

exit((data, copy))
