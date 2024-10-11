# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
y = bincount_ops.sparse_bincount(
    x,
    weights=weights,
    minlength=minlength,
    maxlength=maxlength,
    binary_output=binary_output,
    axis=axis)
self.assertAllEqual(expected_indices, y.indices)
self.assertAllEqual(expected_values, y.values)
self.assertAllEqual(expected_shape, y.dense_shape)
