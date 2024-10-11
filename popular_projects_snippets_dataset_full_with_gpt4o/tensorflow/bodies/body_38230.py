# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Check clip_by_average_norm(t) is the same as
# clip_by_norm(t, clip_norm * tf.compat.v1.to_float(tf.size(t)))
with self.session():
    x = constant_op.constant([-3.0, 0.0, 0.0, 4.0, 0.0, 0.0], shape=[2, 3])
    # Average norm of x = sqrt(3^2 + 4^2) / 6 = 0.83333333
    # expected answer [[-2.88, 0.0, 0.0], [3.84, 0.0, 0.0]]
    clip_norm = constant_op.constant(0.8)
    with_norm = clip_ops.clip_by_average_norm(x, clip_norm)
    without_norm = clip_ops.clip_by_norm(
        x, clip_norm * math_ops.cast(array_ops.size(x), dtypes.float32))
    clip_by_average_norm_ans = self.evaluate(with_norm)
    clip_by_norm_ans = self.evaluate(without_norm)
    self.assertAllClose(clip_by_average_norm_ans, clip_by_norm_ans)
