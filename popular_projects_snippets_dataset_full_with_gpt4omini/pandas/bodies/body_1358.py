# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#10043 this is fundamentally a test for iloc, but test loc while
#  we're here
rw_array = np.eye(10)
rw_df = DataFrame(rw_array)

ro_array = np.eye(10)
ro_array.setflags(write=False)
ro_df = DataFrame(ro_array)

tm.assert_frame_equal(indexer(rw_df)[[1, 2, 3]], indexer(ro_df)[[1, 2, 3]])
tm.assert_frame_equal(indexer(rw_df)[[1]], indexer(ro_df)[[1]])
tm.assert_series_equal(indexer(rw_df)[1], indexer(ro_df)[1])
tm.assert_frame_equal(indexer(rw_df)[1:3], indexer(ro_df)[1:3])
