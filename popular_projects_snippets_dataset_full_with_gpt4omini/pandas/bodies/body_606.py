# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_find_common_type.py
dtype = PeriodDtype(freq="D")
assert find_common_type([dtype, dtype2]) == object
assert find_common_type([dtype2, dtype]) == object
