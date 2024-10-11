# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
rng = period_range("2007-01", freq="M", periods=10)

assert Period("2007-01", freq="M") in rng
assert Period("2007-01", freq="D") not in rng
assert Period("2007-01", freq="2M") not in rng
