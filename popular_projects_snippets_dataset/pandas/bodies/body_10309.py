# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
# Regression test from GH 10448.

out = np.array([[np.nan]], dtype=self.dtype)
counts = np.array([0], dtype="int64")
values = 0.832845131556193 * np.ones((3, 1), dtype=self.dtype)
labels = np.zeros(3, dtype="intp")

self.algo(out, counts, values, labels)

assert counts[0] == 3
assert out[0, 0] >= 0
tm.assert_almost_equal(out[0, 0], 0.0)
