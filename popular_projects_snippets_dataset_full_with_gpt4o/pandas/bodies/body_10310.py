# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
prng = np.random.RandomState(1234)

out = np.array([[np.nan]], dtype=self.dtype)
counts = np.array([0], dtype="int64")
values = (prng.rand(10**6) + 10**12).astype(self.dtype)
values.shape = (10**6, 1)
labels = np.zeros(10**6, dtype="intp")

self.algo(out, counts, values, labels)

assert counts[0] == 10**6
tm.assert_almost_equal(out[0, 0], 1.0 / 12, rtol=0.5e-3)
