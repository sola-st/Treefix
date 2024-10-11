# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
a = pd.array([1, None], dtype=Float64Dtype())
assert a[1] is pd.NA
