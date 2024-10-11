# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

# GH #492
col = np.arange(10)
idx = [(0.0, 1.0), (2.0, 3.0), (4.0, 5.0)]
data = np.random.randn(30).reshape((3, 10))
DF = DataFrame(data, index=idx, columns=col)

with catch_warnings(record=True):
    simplefilter("ignore", pd.errors.PerformanceWarning)
    _check_roundtrip(DF, tm.assert_frame_equal, path=setup_path)
