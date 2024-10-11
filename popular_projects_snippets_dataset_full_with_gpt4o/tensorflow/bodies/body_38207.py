# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# TODO(b/78016351): Enable test on GPU once the bug is fixed.
with self.cached_session():
    x = constant_op.constant([float('NaN'), float('Inf'), -float('Inf')])
    np_ans = [float('NaN'), 4.0, -4.0]
    clip_value = 4.0
    ans = clip_ops.clip_by_value(x, -clip_value, clip_value)
    tf_ans = self.evaluate(ans)

self.assertAllClose(np_ans, tf_ans)
