# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Tick-like 3 Days
other = three_days
rng = period_range("2014-05-01", "2014-05-15", freq="D")
expected = period_range("2014-04-28", "2014-05-12", freq="D")

result = rng - other
tm.assert_index_equal(result, expected)

rng -= other
tm.assert_index_equal(rng, expected)
