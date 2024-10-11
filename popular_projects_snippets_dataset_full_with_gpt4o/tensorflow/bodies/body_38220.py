# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Norm clipping when clip_norm < 5
with self.session():
    x0 = constant_op.constant([-2.0, 0.0, 0.0, 4.0, 0.0, 0.0], shape=[2, 3])
    x1 = constant_op.constant([1.0, -2.0])
    # Global norm of x0 and x1 = sqrt(1 + 4^2 + 2^2 + 2^2) = 5
    clip_norm = 4.0

    # Answers are the original tensors scaled by 4.0/5.0
    np_ans_0 = [[-1.6, 0.0, 0.0], [3.2, 0.0, 0.0]]
    np_ans_1 = [0.8, -1.6]

    ans, norm = clip_ops.clip_by_global_norm((x0, None, x1, None), clip_norm)
    self.assertTrue(ans[1] is None)
    self.assertTrue(ans[3] is None)
    tf_ans_1 = self.evaluate(ans[0])
    tf_ans_2 = self.evaluate(ans[2])
    tf_norm = self.evaluate(norm)

self.assertAllClose(tf_norm, 5.0)
self.assertAllClose(np_ans_0, tf_ans_1)
self.assertAllClose(np_ans_1, tf_ans_2)
