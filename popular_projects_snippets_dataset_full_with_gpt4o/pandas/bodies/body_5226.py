# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
result = to_timedelta("nat").to_numpy()
assert result.dtype.kind == "M"
assert result.astype("int64") == iNaT

result = to_timedelta("nan").to_numpy()
assert result.dtype.kind == "M"
assert result.astype("int64") == iNaT
