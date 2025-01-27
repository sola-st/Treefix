# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertRaises(
    ValueError,
    init_ops.random_normal_initializer,
    0.0,
    1.0,
    dtype=dtypes.string)
