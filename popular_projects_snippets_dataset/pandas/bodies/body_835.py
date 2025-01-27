# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr("a: category")
mgr2 = tm.round_trip_pickle(mgr)
tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))

smgr = create_single_mgr("category")
smgr2 = tm.round_trip_pickle(smgr)
tm.assert_series_equal(Series(smgr), Series(smgr2))
