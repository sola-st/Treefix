# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
for axes_value in [1, 2], [[1], [2]], [[], []], 0:
    np_a = np.ones((3, 3))
    np_b = np.array([2, 3, 1])[None, None]
    np_ans = np.tensordot(np_a, np_b, axes_value)

    tf_a = array_ops.ones((3, 3), dtype=dtypes.float32)
    tf_b = constant_op.constant([2, 3, 1], dtype=dtypes.float32)[None, None]
    tf_ans = math_ops.tensordot(tf_a, tf_b, axes_value)

    self.assertAllEqual(tf_ans.shape, np_ans.shape)
    self.assertAllEqual(self.evaluate(tf_ans), np_ans)
