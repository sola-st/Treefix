# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
prng = np.random.RandomState(1234)

out = (np.nan * np.ones((5, 2))).astype(self.dtype)
counts = np.zeros(5, dtype="int64")
values = 10 * prng.rand(10, 2).astype(self.dtype)
values[:, 1] = np.nan
labels = np.tile(np.arange(5), (2,)).astype("intp")

expected_out = np.vstack(
    [
        values[:, 0].reshape(5, 2, order="F").std(ddof=1, axis=1) ** 2,
        np.nan * np.ones(5),
    ]
).T.astype(self.dtype)
expected_counts = counts + 2

self.algo(out, counts, values, labels)
tm.assert_almost_equal(out, expected_out, rtol=0.5e-06)
tm.assert_numpy_array_equal(counts, expected_counts)
