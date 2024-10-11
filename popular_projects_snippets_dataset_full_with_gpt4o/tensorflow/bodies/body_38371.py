# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
reduction_axes = constant_op.constant([0, 0])
c = constant_op.constant([1.0, 2.0])
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    ".*Axes contains duplicate dimension: 0.*"):
    self.evaluate(math_ops.reduce_sum(c, reduction_axes))
