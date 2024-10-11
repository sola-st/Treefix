# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
a = ragged_factory_ops.constant([[1, 2], [3]])
b = ragged_factory_ops.constant([[4, 5], [3]])
c = 2
d = ragged_factory_ops.constant([[4, 5], [3, 2, 1]])

if tf2.enabled() and ops.executing_eagerly_outside_functions():
    # Value-based equality:
    self.assertAllEqual(
        math_ops.tensor_equals(a, b), [[False, False], [True]])
    self.assertAllEqual(
        math_ops.tensor_not_equals(a, b), [[True, True], [False]])

    # Value-based equality (w/ broadcasting):
    self.assertAllEqual(
        math_ops.tensor_equals(a, c), [[False, True], [False]])
    self.assertAllEqual(
        math_ops.tensor_not_equals(a, c), [[True, False], [True]])
    self.assertFalse(math_ops.tensor_equals(a, d),
                     msg='not broadcast-compatible')
    self.assertTrue(math_ops.tensor_not_equals(a, d),
                    msg='not broadcast-compatible')
else:
    # Identity-based equality:
    self.assertAllEqual(math_ops.tensor_equals(a, a), True)
    self.assertAllEqual(math_ops.tensor_equals(a, b), False)
    self.assertAllEqual(math_ops.tensor_not_equals(a, b), True)
