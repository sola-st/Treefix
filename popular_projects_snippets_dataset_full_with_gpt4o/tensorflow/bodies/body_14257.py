# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x_ragged = ragged_factory_ops.constant(x)
w = ragged_factory_ops.constant(weights) if weights is not None else None
y = bincount_ops.sparse_bincount(
    x_ragged,
    weights=w,
    minlength=minlength,
    maxlength=maxlength,
    binary_output=binary_output,
    axis=axis)
self.assertAllEqual(expected_indices, y.indices)
self.assertAllEqual(expected_values, y.values)
self.assertAllEqual(expected_shape, y.dense_shape)
