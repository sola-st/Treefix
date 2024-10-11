# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# No norm clipping when average clip_norm = 0
with self.session():
    x = constant_op.constant([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], shape=[2, 3])
    # Average norm = 0, no changes
    np_ans = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    clip_norm = 0.9
    ans = clip_ops.clip_by_average_norm(x, clip_norm)
    tf_ans = self.evaluate(ans)

self.assertAllClose(np_ans, tf_ans)
