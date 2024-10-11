# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Asserts that two values are equal."""
if isinstance(expected, dict):
    self.assertItemsEqual(list(expected.keys()), list(actual.keys()))
    for k in expected.keys():
        self.assertValuesEqual(expected[k], actual[k])
elif sparse_tensor.is_sparse(expected):
    self.assertAllEqual(expected.indices, actual.indices)
    self.assertAllEqual(expected.values, actual.values)
    self.assertAllEqual(expected.dense_shape, actual.dense_shape)
else:
    self.assertAllEqual(expected, actual)
