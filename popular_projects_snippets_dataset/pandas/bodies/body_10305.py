# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
prng = np.random.RandomState(1234)

out = (np.nan * np.ones((5, 1))).astype(self.dtype)
counts = np.zeros(5, dtype="int64")
values = 10 * prng.rand(15, 1).astype(self.dtype)
labels = np.tile(np.arange(5), (3,)).astype("intp")

expected_out = (
    np.squeeze(values).reshape((5, 3), order="F").std(axis=1, ddof=1) ** 2
)[:, np.newaxis]
expected_counts = counts + 3

self.algo(out, counts, values, labels)
assert np.allclose(out, expected_out, self.rtol)
tm.assert_numpy_array_equal(counts, expected_counts)
