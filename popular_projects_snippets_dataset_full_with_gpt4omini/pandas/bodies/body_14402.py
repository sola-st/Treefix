# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

unicode_values = ["\u03c3", "\u03c3\u03c3"]

# PerformanceWarning
with catch_warnings(record=True):
    simplefilter("ignore", pd.errors.PerformanceWarning)
    s = Series(np.random.randn(len(unicode_values)), unicode_values)
    _check_roundtrip(s, tm.assert_series_equal, path=setup_path)
