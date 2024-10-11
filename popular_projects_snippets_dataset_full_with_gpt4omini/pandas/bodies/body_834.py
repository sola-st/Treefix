# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr(mgr_string)
mgr2 = tm.round_trip_pickle(mgr)
tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))
