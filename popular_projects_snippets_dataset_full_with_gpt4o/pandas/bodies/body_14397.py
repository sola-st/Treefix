# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
frame = multiindex_dataframe_random_data

_check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(frame.T, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(frame["A"], tm.assert_series_equal, path=setup_path)

# check that the names are stored
with ensure_clean_store(setup_path) as store:
    store["frame"] = frame
    recons = store["frame"]
    tm.assert_frame_equal(recons, frame)
