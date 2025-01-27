# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_find_common_type.py
dtype = DatetimeTZDtype(unit="ns", tz="US/Eastern")
assert find_common_type([dtype, dtype]) == "datetime64[ns, US/Eastern]"
