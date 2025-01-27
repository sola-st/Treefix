# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
other = two_hours
rng = period_range("2014-01-01 10:00", "2014-01-05 10:00", freq="H")
expected = period_range("2014-01-01 12:00", "2014-01-05 12:00", freq="H")

result = rng + other
tm.assert_index_equal(result, expected)

rng += other
tm.assert_index_equal(rng, expected)
