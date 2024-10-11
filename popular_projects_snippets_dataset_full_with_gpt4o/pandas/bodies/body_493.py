# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# though PeriodDtype has object kind, it cannot be string
assert not is_string_dtype(PeriodDtype("D"))
