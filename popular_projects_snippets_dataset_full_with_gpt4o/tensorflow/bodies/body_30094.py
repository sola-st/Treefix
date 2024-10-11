# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x_np = np.array([1, 200, 3, 40, 5], dtype=np_dtype)

for use_gpu in [False, True]:
    for axis_dtype in [dtypes.int32, dtypes.int64]:
        with self.subTest(use_gpu=use_gpu, axis_dtype=axis_dtype):
            x_tf = self.evaluate(
                array_ops.reverse_v2(x_np,
                                     constant_op.constant([0], dtype=axis_dtype)))
            self.assertAllEqual(x_tf, np.asarray(x_np)[::-1])
