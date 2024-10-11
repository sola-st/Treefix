# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# offset
# DateOffset
rng = period_range("2014", "2024", freq="A")
result = rng + pd.offsets.YearEnd(5)
expected = period_range("2019", "2029", freq="A")
tm.assert_index_equal(result, expected)
rng += pd.offsets.YearEnd(5)
tm.assert_index_equal(rng, expected)
