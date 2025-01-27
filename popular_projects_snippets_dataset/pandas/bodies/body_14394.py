# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
s0 = Series(dtype=object)
s1 = Series(name="myseries", dtype=object)
df0 = DataFrame()
df1 = DataFrame(index=["a", "b", "c"])
df2 = DataFrame(columns=["d", "e", "f"])

_check_roundtrip(s0, tm.assert_series_equal, path=setup_path)
_check_roundtrip(s1, tm.assert_series_equal, path=setup_path)
_check_roundtrip(df0, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(df1, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(df2, tm.assert_frame_equal, path=setup_path)
