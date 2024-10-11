# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# No norm clipping when norm = 0
with self.session():
    x0 = constant_op.constant([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], shape=[2, 3])
    x1 = constant_op.constant([0.0, 0.0])
    # Norm = 0, no changes
    np_ans_0 = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    np_ans_1 = [0.0, 0.0]
    clip_norm = 6.0

    ans, norm = clip_ops.clip_by_global_norm([x0, x1], clip_norm)
    tf_ans_1 = self.evaluate(ans[0])
    tf_ans_2 = self.evaluate(ans[1])
    tf_norm = self.evaluate(norm)

self.assertAllClose(tf_norm, 0.0)
self.assertAllClose(np_ans_0, tf_ans_1)
self.assertAllClose(np_ans_1, tf_ans_2)
