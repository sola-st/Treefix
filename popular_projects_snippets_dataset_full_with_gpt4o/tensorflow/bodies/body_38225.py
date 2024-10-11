# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Expect all NaNs when global norm is inf.
with self.session():
    x0 = constant_op.constant([-2.0, 0.0, np.inf, 4.0, 0.0, 0.0],
                              shape=[2, 3])
    x1 = constant_op.constant([1.0, -2.0])
    clip_norm = 6.0

    ans, norm = clip_ops.clip_by_global_norm([x0, x1], clip_norm)
    tf_ans_1 = self.evaluate(ans[0])
    tf_ans_2 = self.evaluate(ans[1])
    tf_norm = self.evaluate(norm)
    self.assertAllEqual(tf_norm, float('inf'))
    self.assertAllEqual(tf_ans_1, np.full([2, 3], float('nan')))
    self.assertAllEqual(tf_ans_2, np.full([2], float('nan')))
