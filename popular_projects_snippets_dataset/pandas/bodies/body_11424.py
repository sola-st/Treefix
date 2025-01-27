# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
ymd = multiindex_year_month_day_dataframe_random_data
frame = multiindex_dataframe_random_data

def _test_roundtrip(frame):
    unpickled = tm.round_trip_pickle(frame)
    tm.assert_frame_equal(frame, unpickled)

_test_roundtrip(frame)
_test_roundtrip(frame.T)
_test_roundtrip(ymd)
_test_roundtrip(ymd.T)
