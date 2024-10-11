# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

df = DataFrame({"a": [1, 2, 3], "b": [1.0, 2.0, 3.0], "c": ["a", "b", "c"]})
ts = tm.makeTimeSeries()
df["d"] = ts.index[:3]
_check_roundtrip(df, tm.assert_frame_equal, path=setup_path)
