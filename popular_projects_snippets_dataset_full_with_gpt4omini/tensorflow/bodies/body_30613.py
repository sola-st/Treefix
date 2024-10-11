# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertRaises(
    ValueError,
    init_ops.convolutional_delta_orthogonal,
    dtype=dtypes.string)
