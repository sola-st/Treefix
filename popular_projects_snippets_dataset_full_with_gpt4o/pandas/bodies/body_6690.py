# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_pickle.py
# https://github.com/pandas-dev/pandas/issues/35658
idx = IntervalIndex.from_tuples([(1, 2), (2, 3)], closed=closed)
result = tm.round_trip_pickle(idx)
tm.assert_index_equal(result, idx)
