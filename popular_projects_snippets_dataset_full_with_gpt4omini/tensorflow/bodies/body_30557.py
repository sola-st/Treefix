# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.uniform_unit_scaling_initializer()
self.assertFalse(duplicated_initializer(self, init, 1))
