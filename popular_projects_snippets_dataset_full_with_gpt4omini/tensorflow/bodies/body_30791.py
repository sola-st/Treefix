# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
op_fns = [
    inplace_ops.inplace_add,
    inplace_ops.inplace_sub,
    inplace_ops.inplace_update,
]
for dtype in [dtypes.float32, dtypes.int32, dtypes.int64]:
    for op_fn in op_fns:
        with test_util.use_gpu():
            x = array_ops.zeros([7, 0], dtype)
            y = np.zeros([7, 0], dtype.as_numpy_dtype)
            self.assertAllClose(x, y)
            x = op_fn(x, [3], array_ops.ones([1, 0], dtype))
            self.assertAllClose(x, y)
            x = op_fn(x, None, array_ops.ones([1, 0], dtype))
            self.assertAllClose(x, y)
