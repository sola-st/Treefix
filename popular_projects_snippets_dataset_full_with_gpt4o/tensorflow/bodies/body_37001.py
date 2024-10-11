# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
self.assertTrue(r.values.shape.is_compatible_with(values))
self.assertTrue(r.row_splits.shape.is_compatible_with(splits))
