# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
# GH #14444 & #13589:  Add support for sort algo choosing
series = Series(index=[3, 2, 1, 4, 3], dtype=object)
expected_series = Series(index=[1, 2, 3, 3, 4], dtype=object)

index_sorted_series = series.sort_index(kind=sort_kind, key=sort_by_key)
tm.assert_series_equal(expected_series, index_sorted_series)
