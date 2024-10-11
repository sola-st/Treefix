# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Check that PeriodArray defers to Index on arithmetic ops
pi = period_range("2000-12-31", periods=3)
parr = pi.array

result = parr - pi
expected = pi - pi
tm.assert_index_equal(result, expected)
