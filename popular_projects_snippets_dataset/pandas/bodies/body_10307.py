# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
prng = np.random.RandomState(1234)

out = (np.nan * np.ones((5, 2))).astype(self.dtype)
counts = np.zeros(5, dtype="int64")
values = 10 * prng.rand(10, 2).astype(self.dtype)
labels = np.tile(np.arange(5), (2,)).astype("intp")

expected_out = np.std(values.reshape(2, 5, 2), ddof=1, axis=0) ** 2
expected_counts = counts + 2

self.algo(out, counts, values, labels)
assert np.allclose(out, expected_out, self.rtol)
tm.assert_numpy_array_equal(counts, expected_counts)
