# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
dtype = IntervalDtype("int64", "left")
assert not is_valid_na_for_dtype(NaT, dtype)

dtype = IntervalDtype("datetime64[ns]", "both")
assert not is_valid_na_for_dtype(NaT, dtype)
