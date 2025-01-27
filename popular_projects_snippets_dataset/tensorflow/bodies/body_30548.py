# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    init1 = init_ops.truncated_normal_initializer(
        0.0, 1.0, seed=1, dtype=dtype)
    init2 = init_ops.truncated_normal_initializer(
        0.0, 1.0, seed=2, dtype=dtype)
    self.assertFalse(identicaltest(self, init1, init2))
