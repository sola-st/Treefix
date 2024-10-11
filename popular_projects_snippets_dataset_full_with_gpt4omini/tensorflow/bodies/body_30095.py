# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x_np = np.array([[1, 200, 3], [4, 5, 60]], dtype=np_dtype)

for reverse_f in [array_ops.reverse_v2, array_ops.reverse]:
    for use_gpu in [False, True]:
        for axis_dtype in [dtypes.int32, dtypes.int64]:
            with self.subTest(
                reverse_f=reverse_f, use_gpu=use_gpu, axis_dtype=axis_dtype):
                x_tf_1 = self.evaluate(
                    reverse_f(x_np, constant_op.constant([0], dtype=axis_dtype)))
                x_tf_2 = self.evaluate(
                    reverse_f(x_np, constant_op.constant([-2], dtype=axis_dtype)))
                x_tf_3 = self.evaluate(
                    reverse_f(x_np, constant_op.constant([1], dtype=axis_dtype)))
                x_tf_4 = self.evaluate(
                    reverse_f(x_np, constant_op.constant([-1], dtype=axis_dtype)))
                x_tf_5 = self.evaluate(
                    reverse_f(x_np, constant_op.constant([1, 0], dtype=axis_dtype)))
                self.assertAllEqual(x_tf_1, np.asarray(x_np)[::-1, :])
                self.assertAllEqual(x_tf_2, np.asarray(x_np)[::-1, :])
                self.assertAllEqual(x_tf_3, np.asarray(x_np)[:, ::-1])
                self.assertAllEqual(x_tf_4, np.asarray(x_np)[:, ::-1])
                self.assertAllEqual(x_tf_5, np.asarray(x_np)[::-1, ::-1])
