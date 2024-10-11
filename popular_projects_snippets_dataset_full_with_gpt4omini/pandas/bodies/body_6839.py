# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# tuple (NA, NA) evaluates the same as NA as an element
na_tuple = [(0, 1), (np.nan, np.nan), (2, 3)]
idx_na_tuple = IntervalIndex.from_tuples(na_tuple)
idx_na_element = IntervalIndex.from_tuples([(0, 1), np.nan, (2, 3)])
tm.assert_index_equal(idx_na_tuple, idx_na_element)
