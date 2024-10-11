# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
rng = period_range("2007-01", periods=50)

result = rng - five
exp = rng + (-five)
tm.assert_index_equal(result, exp)
