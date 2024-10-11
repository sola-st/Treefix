# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
a = pd.Series([1, 2]).set_flags(allows_duplicate_labels=False)
b = tm.round_trip_pickle(a)
tm.assert_series_equal(a, b)

a = pd.DataFrame({"A": []}).set_flags(allows_duplicate_labels=False)
b = tm.round_trip_pickle(a)
tm.assert_frame_equal(a, b)
