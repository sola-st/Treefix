# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    with self.subTest(dtype=dtype, use_gpu=True):
        x = constant_op.constant([3, 4, 0, 2, 1], dtype=dtype)
        y = array_ops.invert_permutation(x)
        self.assertAllEqual(y.get_shape(), [5])
        self.assertAllEqual(y, [2, 4, 3, 0, 1])
