# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
datetime_series.index = datetime_series.index._with_freq(None)

# For GH#11402
rindex = list(datetime_series.index)
random.shuffle(rindex)

# descending
random_order = datetime_series.reindex(rindex)
result = random_order.sort_index(ascending=False, inplace=True)

assert result is None
expected = datetime_series.reindex(datetime_series.index[::-1])
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(random_order, expected)

# ascending
random_order = datetime_series.reindex(rindex)
result = random_order.sort_index(ascending=True, inplace=True)

assert result is None
expected = datetime_series.copy()
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(random_order, expected)
