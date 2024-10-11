# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
res = ts.to_numpy()
assert res == dt64
assert res.dtype == dt64.dtype
