# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.truncated_normal_initializer(0.0, 1.0)
self.assertFalse(duplicated_initializer(self, init, 1))
