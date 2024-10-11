# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# No norm clipping when average clip_norm >= 0.83333333
with self.session():
    x = constant_op.constant([-3.0, 0.0, 0.0, 4.0, 0.0, 0.0], shape=[2, 3])
    # Average norm of x = sqrt(3^2 + 4^2) / 6 = 0.83333333
    np_ans = [[-3.0, 0.0, 0.0], [4.0, 0.0, 0.0]]
    clip_norm = 0.9
    ans = clip_ops.clip_by_average_norm(x, clip_norm)
    tf_ans = self.evaluate(ans)

self.assertAllClose(np_ans, tf_ans)
