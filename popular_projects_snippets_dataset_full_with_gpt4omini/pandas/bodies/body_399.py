# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_datetime64tz_dtype(object)
assert not com.is_datetime64tz_dtype([1, 2, 3])
assert not com.is_datetime64tz_dtype(pd.DatetimeIndex([1, 2, 3]))
assert com.is_datetime64tz_dtype(pd.DatetimeIndex(["2000"], tz="US/Eastern"))
