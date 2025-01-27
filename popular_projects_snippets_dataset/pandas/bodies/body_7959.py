# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
result = period_range("2007-01", periods=10.5, freq="M")
exp = period_range("2007-01", periods=10, freq="M")
tm.assert_index_equal(result, exp)
