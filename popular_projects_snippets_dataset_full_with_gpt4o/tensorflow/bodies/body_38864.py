# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
self.assertAllEqual(expected_tensor.indices, result.indices)
self.assertAllEqual(expected_tensor.values, result.values)
if (result.dense_shape is not None and
    expected_tensor.dense_shape is not None):
    self.assertAllEqual(expected_tensor.dense_shape, result.dense_shape)
