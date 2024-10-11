# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in [dtypes.int32, dtypes.int64, dtypes.float32, dtypes.float64]:
    with self.subTest(dtype=dtype, use_gpu=True):
        x = constant_op.constant([0, 1, 2, 3], dtype=dtype)
        y = gen_array_ops.snapshot(x)
        self.assertAllEqual(y, [0, 1, 2, 3])
