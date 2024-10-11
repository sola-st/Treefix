# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex_like.py
other = datetime_series[::2]
tm.assert_series_equal(
    datetime_series.reindex(other.index), datetime_series.reindex_like(other)
)

# GH#7179
day1 = datetime(2013, 3, 5)
day2 = datetime(2013, 5, 5)
day3 = datetime(2014, 3, 5)

series1 = Series([5, None, None], [day1, day2, day3])
series2 = Series([None, None], [day1, day3])

result = series1.reindex_like(series2, method="pad")
expected = Series([5, np.nan], index=[day1, day3])
tm.assert_series_equal(result, expected)
