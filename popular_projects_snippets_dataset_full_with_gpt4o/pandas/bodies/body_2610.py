# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
empty_frame = DataFrame()

unpickled = tm.round_trip_pickle(float_string_frame)
tm.assert_frame_equal(float_string_frame, unpickled)

# buglet
float_string_frame._mgr.ndim

# empty
unpickled = tm.round_trip_pickle(empty_frame)
repr(unpickled)

# tz frame
unpickled = tm.round_trip_pickle(timezone_frame)
tm.assert_frame_equal(timezone_frame, unpickled)
