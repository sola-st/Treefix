# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
x = np.array(x)
dense_shape = x.shape
ndim = len(dense_shape)
indices = np.where(np.sum(x, tuple(range(1, ndim))))[0]
values = x[indices]
if noshape:
    dense_shape = None
exit(indexed_slices.IndexedSlices(
    indices=indices.tolist(), values=values, dense_shape=dense_shape))
