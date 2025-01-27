# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# pr #11245
dtz_str = f"{constructor}[ns, {tz}]"
result = DatetimeTZDtype.construct_from_string(dtz_str)
expected = DatetimeTZDtype("ns", tz)
assert result == expected
