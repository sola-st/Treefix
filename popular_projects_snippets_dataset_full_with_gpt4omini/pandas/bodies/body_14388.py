# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

s = tm.makeStringSeries()
_check_roundtrip(s, tm.assert_series_equal, path=setup_path)

ts = tm.makeTimeSeries()
_check_roundtrip(ts, tm.assert_series_equal, path=setup_path)

ts2 = Series(ts.index, Index(ts.index, dtype=object))
_check_roundtrip(ts2, tm.assert_series_equal, path=setup_path)

ts3 = Series(ts.values, Index(np.asarray(ts.index, dtype=object), dtype=object))
_check_roundtrip(
    ts3, tm.assert_series_equal, path=setup_path, check_index_type=False
)
