# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

# GH #454
index = np.random.randn(10)
s = Series(np.random.randn(10), index=index)
_check_roundtrip(s, tm.assert_series_equal, path=setup_path)
