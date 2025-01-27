# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
result = na_value_for_dtype(dtype)
# identify check doesn't work for datetime64/timedelta64("NaT") bc they
#  are not singletons
assert result is na_value or (
    isna(result) and isna(na_value) and type(result) is type(na_value)
)
