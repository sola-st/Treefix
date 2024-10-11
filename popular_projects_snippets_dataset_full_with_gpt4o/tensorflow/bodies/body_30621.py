# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertRaises(
    ValueError, init_ops.convolutional_orthogonal_1d, dtype=dtypes.string)
