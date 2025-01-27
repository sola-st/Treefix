# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
t = math_ops._as_indexed_slices(
    constant_op.constant([[1., 2.], [0, 0], [3., 4.]]))
self.assertTrue(cross_device_utils.is_indexed_slices(t))
