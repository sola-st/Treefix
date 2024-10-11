# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_datetime_or_timedelta_dtype(int)
assert not com.is_datetime_or_timedelta_dtype(str)
assert not com.is_datetime_or_timedelta_dtype(pd.Series([1, 2]))
assert not com.is_datetime_or_timedelta_dtype(np.array(["a", "b"]))

# TODO(jreback), this is slightly suspect
assert not com.is_datetime_or_timedelta_dtype(DatetimeTZDtype("ns", "US/Eastern"))

assert com.is_datetime_or_timedelta_dtype(np.datetime64)
assert com.is_datetime_or_timedelta_dtype(np.timedelta64)
assert com.is_datetime_or_timedelta_dtype(np.array([], dtype=np.timedelta64))
assert com.is_datetime_or_timedelta_dtype(np.array([], dtype=np.datetime64))
