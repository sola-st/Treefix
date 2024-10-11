# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# offset
# DateOffset
rng = period_range("2014", "2024", freq="A")
result = rng - pd.offsets.YearEnd(5)
expected = period_range("2009", "2019", freq="A")
tm.assert_index_equal(result, expected)
rng -= pd.offsets.YearEnd(5)
tm.assert_index_equal(rng, expected)

rng = period_range("2014-01", "2016-12", freq="M")
result = rng - pd.offsets.MonthEnd(5)
expected = period_range("2013-08", "2016-07", freq="M")
tm.assert_index_equal(result, expected)

rng -= pd.offsets.MonthEnd(5)
tm.assert_index_equal(rng, expected)
