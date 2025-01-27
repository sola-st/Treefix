# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
arr = np.random.randn(1000)

# We store the bins as Index that have been
# rounded to comparisons are a bit tricky.
labels, _ = qcut(arr, 4, retbins=True)
ex_bins = np.quantile(arr, [0, 0.25, 0.5, 0.75, 1.0])

result = labels.categories.left.values
assert np.allclose(result, ex_bins[:-1], atol=1e-2)

result = labels.categories.right.values
assert np.allclose(result, ex_bins[1:], atol=1e-2)

ex_levels = cut(arr, ex_bins, include_lowest=True)
tm.assert_categorical_equal(labels, ex_levels)
