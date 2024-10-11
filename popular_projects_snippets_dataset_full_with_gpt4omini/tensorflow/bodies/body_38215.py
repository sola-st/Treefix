# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Norm clipping when clip_norm < 5
with self.session():
    x = constant_op.constant([-3.0, 0.0, 0.0, 4.0, 0.0, 3.0], shape=[2, 3])
    # Norm of x[:, 0] = sqrt(3^2 + 4^2) = 5, x[:, 2] = 3
    np_ans = [[-2.4, 0.0, 0.0], [3.2, 0.0, 3.0]]
    clip_norm = 4.0
    ans = clip_ops.clip_by_norm(x, clip_norm, [0])
    tf_ans = self.evaluate(ans)

self.assertAllClose(np_ans, tf_ans)
