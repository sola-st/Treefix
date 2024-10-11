# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.orthogonal_initializer()
self.assertFalse(duplicated_initializer(self, init, 1, (10, 10)))
