# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    init1 = init_ops.uniform_unit_scaling_initializer(seed=1, dtype=dtype)
    init2 = init_ops.uniform_unit_scaling_initializer(seed=2, dtype=dtype)
    init3 = init_ops.uniform_unit_scaling_initializer(
        1.5, seed=1, dtype=dtype)
    self.assertFalse(identicaltest(self, init1, init2))
    self.assertFalse(identicaltest(self, init1, init3))
    self.assertFalse(identicaltest(self, init2, init3))
