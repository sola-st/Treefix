# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
series = Series(index=[3, 2, 1, 4, 3, np.nan], dtype=object)
expected_series_first = Series(index=[np.nan, 1, 2, 3, 3, 4], dtype=object)

index_sorted_series = series.sort_index(na_position="first")
tm.assert_series_equal(expected_series_first, index_sorted_series)

expected_series_last = Series(index=[1, 2, 3, 3, 4, np.nan], dtype=object)

index_sorted_series = series.sort_index(na_position="last")
tm.assert_series_equal(expected_series_last, index_sorted_series)
