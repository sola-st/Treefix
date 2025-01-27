# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# GH 5348: "ValueError: Could not evaluate WOM-1SUN" shouldn't raise
d1 = date(2002, 9, 1)
d2 = date(2013, 10, 27)
d3 = date(2012, 9, 30)
idx1 = DatetimeIndex([d1, d2])
idx2 = DatetimeIndex([d3])
result_append = idx1.append(idx2)
expected = DatetimeIndex([d1, d2, d3])
tm.assert_index_equal(result_append, expected)
result_union = idx1.union(idx2)
expected = DatetimeIndex([d1, d3, d2])
tm.assert_index_equal(result_union, expected)

# GH 5115
result = date_range("2013-1-1", periods=4, freq="WOM-1SAT")
dates = ["2013-01-05", "2013-02-02", "2013-03-02", "2013-04-06"]
expected = DatetimeIndex(dates, freq="WOM-1SAT")
tm.assert_index_equal(result, expected)
