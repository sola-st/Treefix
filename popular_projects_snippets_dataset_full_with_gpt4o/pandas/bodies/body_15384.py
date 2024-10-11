# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
mask = string_series > string_series.median()

# similar indexed series
result = string_series.copy()
result[mask] = string_series * 2
expected = string_series * 2
tm.assert_series_equal(result[mask], expected[mask])

# needs alignment
result = string_series.copy()
result[mask] = (string_series * 2)[0:5]
expected = (string_series * 2)[0:5].reindex_like(string_series)
expected[-mask] = string_series[mask]
tm.assert_series_equal(result[mask], expected[mask])
