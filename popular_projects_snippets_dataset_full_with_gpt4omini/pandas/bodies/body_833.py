# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py

mgr2 = tm.round_trip_pickle(mgr)
tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))

# GH2431
assert hasattr(mgr2, "_is_consolidated")
assert hasattr(mgr2, "_known_consolidated")

# reset to False on load
assert not mgr2._is_consolidated
assert not mgr2._known_consolidated
