# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH-43693: Check float64 preservation when >= 16,777,217
series = Series([16777217.0, np.finfo(np.float64).max, np.nan], dtype=np.float64)
result = to_numeric(series, downcast="float")

assert series.dtype == result.dtype
