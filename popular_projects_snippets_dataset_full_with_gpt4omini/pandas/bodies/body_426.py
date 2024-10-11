# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.needs_i8_conversion(str)
assert not com.needs_i8_conversion(np.int64)
assert not com.needs_i8_conversion(pd.Series([1, 2]))
assert not com.needs_i8_conversion(np.array(["a", "b"]))

assert com.needs_i8_conversion(np.datetime64)
assert com.needs_i8_conversion(pd.Series([], dtype="timedelta64[ns]"))
assert com.needs_i8_conversion(pd.DatetimeIndex(["2000"], tz="US/Eastern"))
