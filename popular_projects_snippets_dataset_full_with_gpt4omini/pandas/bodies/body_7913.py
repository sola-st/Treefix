# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period_range.py
# non-empty
expected = date_range(
    start="2017-01-01", periods=5, freq=freq, name="foo"
).to_period()
start, end = str(expected[0]), str(expected[-1])

result = period_range(start=start, end=end, freq=freq, name="foo")
tm.assert_index_equal(result, expected)

result = period_range(start=start, periods=5, freq=freq, name="foo")
tm.assert_index_equal(result, expected)

result = period_range(end=end, periods=5, freq=freq, name="foo")
tm.assert_index_equal(result, expected)

# empty
expected = PeriodIndex([], freq=freq, name="foo")

result = period_range(start=start, periods=0, freq=freq, name="foo")
tm.assert_index_equal(result, expected)

result = period_range(end=end, periods=0, freq=freq, name="foo")
tm.assert_index_equal(result, expected)

result = period_range(start=end, end=start, freq=freq, name="foo")
tm.assert_index_equal(result, expected)
