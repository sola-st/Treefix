# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.session():
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([5], maxlength=3)), [0, 0, 0])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([1], maxlength=3)), [0, 1])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([], maxlength=3)), [])
