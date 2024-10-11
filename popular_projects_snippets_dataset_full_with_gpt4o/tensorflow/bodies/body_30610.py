# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    init1 = init_ops.convolutional_delta_orthogonal(seed=1, dtype=dtype)
    init2 = init_ops.convolutional_delta_orthogonal(seed=1, dtype=dtype)
    self.assertTrue(identicaltest(self, init1, init2, (3, 3, 10, 10)))
