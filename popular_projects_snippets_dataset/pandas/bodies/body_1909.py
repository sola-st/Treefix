# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# conforms, but different month
ts = simple_period_range_series("1990", "1992", freq="A-JUN")
result = ts.resample("Q-MAR", convention=how).ffill()
expected = ts.asfreq("Q-MAR", how=how)
expected = expected.reindex(result.index, method="ffill")

# .to_timestamp('D')
# expected = expected.resample('Q-MAR').ffill()

tm.assert_series_equal(result, expected)
