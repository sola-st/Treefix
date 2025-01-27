# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# GH#26916
ts = fixed_now_ts
dt64 = np.datetime64("2016-01-01", "ns")
arr = np.array(dt64)
assert arr.ndim == 0

result = arr < ts
assert result is np.bool_(True)
result = arr > ts
assert result is np.bool_(False)
