# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators_test.py
a = ragged_factory_ops.constant([[1, 2], [3]])
b = ragged_factory_ops.constant([[4, 5], [3]])
c = 2

if tf2.enabled() and ops.executing_eagerly_outside_functions():
    # Value-based equality:
    self.assertAllEqual(a == b, [[False, False], [True]])
    self.assertAllEqual(a != b, [[True, True], [False]])

    # Value-based equality (w/ broadcasting):
    self.assertAllEqual(a == c, [[False, True], [False]])
    self.assertAllEqual(a != c, [[True, False], [True]])
else:
    # Identity-based equality:
    self.assertAllEqual(a == b, False)
    self.assertAllEqual(a != b, True)
