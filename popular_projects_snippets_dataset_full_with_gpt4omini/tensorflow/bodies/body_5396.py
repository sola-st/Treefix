# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
t = math_ops._as_indexed_slices(
    constant_op.constant([[1., 2.], [0, 0], [3., 4.]]))
n = 2
expected = constant_op.constant([[0.5, 1.], [0, 0], [1.5, 2.]])
result = cross_device_utils.divide_by_n_tensors_or_indexed_slices(t, n)
self.assertIsInstance(result, indexed_slices.IndexedSlices)
self._assert_values_equal(expected, result)
