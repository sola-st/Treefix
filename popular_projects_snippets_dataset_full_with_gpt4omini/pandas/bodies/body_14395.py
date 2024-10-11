# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
s = Series(dtype=dtype)
_check_roundtrip(s, tm.assert_series_equal, path=setup_path)
