# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
self.assertTrue(r.indices.shape.is_compatible_with(indices))
self.assertTrue(r.values.shape.is_compatible_with(values))
self.assertTrue(r.dense_shape.shape.is_compatible_with(dense_shape))
