# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Test case for GitHub issue 18712
with self.cached_session() as sess:
    v = math_ops.count_nonzero(constant_op.constant(["test"]))
    self.assertAllClose(self.evaluate(v), 1)
