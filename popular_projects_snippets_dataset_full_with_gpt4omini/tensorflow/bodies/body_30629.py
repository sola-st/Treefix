# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.convolutional_orthogonal_2d()
self.assertFalse(duplicated_initializer(self, init, 1, (3, 3, 10, 10)))
