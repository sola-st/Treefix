# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
prng = np.random.RandomState(1234)

out = (np.nan * np.ones((1, 1))).astype(self.dtype)
counts = np.zeros(1, dtype="int64")
values = 10 * prng.rand(5, 1).astype(self.dtype)
labels = np.zeros(5, dtype="intp")

expected_out = np.array([[values.std(ddof=1) ** 2]])
expected_counts = counts + 5

self.algo(out, counts, values, labels)

assert np.allclose(out, expected_out, self.rtol)
tm.assert_numpy_array_equal(counts, expected_counts)
