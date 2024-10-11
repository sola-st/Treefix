# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
t0 = math_ops._as_indexed_slices(
    constant_op.constant([[1., 2.], [0, 0], [3., 4.]]))
t1 = math_ops._as_indexed_slices(
    constant_op.constant([[0., 0.], [5, 6], [7., 8.]]))
total = constant_op.constant([[1., 2.], [5, 6], [10., 12.]])
result = cross_device_utils.aggregate_tensors_or_indexed_slices([t0, t1])
self.assertIsInstance(result, indexed_slices.IndexedSlices)
self._assert_values_equal(total, result)
