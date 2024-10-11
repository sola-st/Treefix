# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
a = pd.array([1, None], dtype=Int64Dtype())
assert a[1] is pd.NA
