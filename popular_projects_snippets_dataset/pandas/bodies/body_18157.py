# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
rng = period_range("2014-01", "2016-12", freq="M")
expected = period_range("2014-06", "2017-05", freq="M")

result = rng + pd.offsets.MonthEnd(5)
tm.assert_index_equal(result, expected)

rng += pd.offsets.MonthEnd(5)
tm.assert_index_equal(rng, expected)
