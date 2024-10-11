# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x_sparse = sparse_ops.from_dense(x)
w_sparse = sparse_ops.from_dense(weights) if weights is not None else None
y = bincount_ops.sparse_bincount(
    x_sparse,
    weights=w_sparse,
    minlength=minlength,
    maxlength=maxlength,
    binary_output=binary_output,
    axis=axis)
self.assertAllEqual(expected_indices, y.indices)
self.assertAllEqual(expected_values, y.values)
self.assertAllEqual(expected_shape, y.dense_shape)
