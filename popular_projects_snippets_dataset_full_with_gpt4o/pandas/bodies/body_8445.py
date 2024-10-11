# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# https://github.com/pandas-dev/pandas/issues/24110
start, end = start_end
result = date_range(start=start, end=end, periods=2, inclusive="left")
expected = DatetimeIndex([start])
tm.assert_index_equal(result, expected)
