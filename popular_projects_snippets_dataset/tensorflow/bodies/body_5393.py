# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
t0 = constant_op.constant([[1., 2.], [0, 0], [3., 4.]])
t1 = constant_op.constant([[0., 0.], [5, 6], [7., 8.]])
total = constant_op.constant([[1., 2.], [5, 6], [10., 12.]])
result = cross_device_utils.aggregate_tensors_or_indexed_slices([t0, t1])
self._assert_values_equal(total, result)
