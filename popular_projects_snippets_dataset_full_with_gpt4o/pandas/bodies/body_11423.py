# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
unpickled = tm.round_trip_pickle(frame)
tm.assert_frame_equal(frame, unpickled)
