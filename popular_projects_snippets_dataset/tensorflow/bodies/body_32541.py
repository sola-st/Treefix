# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# A tensor is non-negative when it satisfies:
#   For every element x_i in x, x_i >= 0
# and an empty tensor has no elements, so this is trivially satisfied.
# This is standard set theory.
empty = constant_op.constant([], name="empty")
with ops.control_dependencies([check_ops.assert_non_negative(empty)]):
    out = array_ops.identity(empty)
self.evaluate(out)
