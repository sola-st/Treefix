# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
for perm_dtype in [np.int64, np.int32]:
    with self.subTest(perm_dtype=perm_dtype):
        x = np.arange(0, 8).reshape([2, 4]).astype(np.float32)
        p = np.array([1, 0]).astype(perm_dtype)
        np_ans = np.copy(x).transpose(p)
        with self.cached_session():
            inx = ops.convert_to_tensor(x)
            inp = constant_op.constant(p)
            y = array_ops.transpose(inx, inp)
            tf_ans = self.evaluate(y)
            self.assertShapeEqual(np_ans, y)
            self.assertAllEqual(np_ans, tf_ans)
