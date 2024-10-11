# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_pickle.py
# GH#11002
# don't infer freq
idx = date_range("1750-1-1", "2050-1-1", freq="7D")
idx_p = tm.round_trip_pickle(idx)
tm.assert_index_equal(idx, idx_p)
