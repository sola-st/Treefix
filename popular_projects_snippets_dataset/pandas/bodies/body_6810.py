# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#30178
rng = period_range("2022-07-01", freq="D", periods=3)
idx = box(interval_range(Timestamp("2022-07-01"), freq="3D", periods=3))

actual = rng.get_indexer(idx)
expected = np.array([-1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(actual, expected)
