# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
with self.cached_session():
    for op in math_ops.argmin, math_ops.argmax:
        ans = op([1]).eval()
        self.assertAllEqual(ans, 0)
