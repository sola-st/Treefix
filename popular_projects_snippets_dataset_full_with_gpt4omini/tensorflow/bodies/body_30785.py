# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
for dtype in [dtypes.float32, dtypes.int32, dtypes.int64, dtypes.bfloat16]:
    with test_util.use_gpu():
        x = array_ops.ones([7, 3], dtype)
        y = np.ones([7, 3], dtype.as_numpy_dtype)
        self.assertAllClose(x, y)
        x = inplace_ops.inplace_sub(x, [3], array_ops.ones([1, 3], dtype))
        y[3, :] -= 1
        self.assertAllClose(x, y)
        x = inplace_ops.inplace_sub(x, [-1], array_ops.ones([1, 3], dtype) * 2)
        y[-1, :] -= 2
        self.assertAllClose(x, y)
        x = inplace_ops.inplace_sub(x, 5, array_ops.ones([3], dtype) * 7)
        y[5, :] -= 7
        self.assertAllClose(x, y)
        x = inplace_ops.inplace_sub(x, None, array_ops.ones([7, 3], dtype) * 99)
        y[:, :] -= 99
        self.assertAllClose(x, y)
