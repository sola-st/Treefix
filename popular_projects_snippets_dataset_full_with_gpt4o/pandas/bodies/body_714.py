# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([np.nan, pd.NaT, np.datetime64("nat")])
assert lib.is_datetime_array(arr)
assert lib.is_datetime64_array(arr)
assert not lib.is_timedelta_or_timedelta64_array(arr)

arr = np.array([np.nan, pd.NaT, np.timedelta64("nat")])
assert not lib.is_datetime_array(arr)
assert not lib.is_datetime64_array(arr)
assert lib.is_timedelta_or_timedelta64_array(arr)

arr = np.array([np.nan, pd.NaT, np.datetime64("nat"), np.timedelta64("nat")])
assert not lib.is_datetime_array(arr)
assert not lib.is_datetime64_array(arr)
assert not lib.is_timedelta_or_timedelta64_array(arr)

arr = np.array([np.nan, pd.NaT])
assert lib.is_datetime_array(arr)
assert lib.is_datetime64_array(arr)
assert lib.is_timedelta_or_timedelta64_array(arr)

arr = np.array([np.nan, np.nan], dtype=object)
assert not lib.is_datetime_array(arr)
assert not lib.is_datetime64_array(arr)
assert not lib.is_timedelta_or_timedelta64_array(arr)

assert lib.is_datetime_with_singletz_array(
    np.array(
        [
            Timestamp("20130101", tz="US/Eastern"),
            Timestamp("20130102", tz="US/Eastern"),
        ],
        dtype=object,
    )
)
assert not lib.is_datetime_with_singletz_array(
    np.array(
        [
            Timestamp("20130101", tz="US/Eastern"),
            Timestamp("20130102", tz="CET"),
        ],
        dtype=object,
    )
)
