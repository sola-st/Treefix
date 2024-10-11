# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# GH#37631
ser = Series(list("abc")).astype("category").iloc[[0]]
res = tm.round_trip_pickle(ser)

assert res._mgr.blocks[0].ndim == 1
assert res._mgr.blocks[0].shape == (1,)

# GH#37631 OP issue was about indexing, underlying problem was pickle
tm.assert_series_equal(res[[True]], ser)
