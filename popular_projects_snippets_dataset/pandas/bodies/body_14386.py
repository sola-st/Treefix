# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
# non-date, non-string index
df = DataFrame(np.random.randn(50, 100))
_check_roundtrip(df, tm.assert_frame_equal, setup_path)
