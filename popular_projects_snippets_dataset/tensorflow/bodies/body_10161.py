# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if (tf2.enabled() and isinstance(float_literal, np.float32) or
    not tf2.enabled() and isinstance(float_literal, float)):
    # TODO(b/199262800): Remove this skip
    self.skipTest("There is a bug in type promotion.")
if is_equals:
    op = math_ops.tensor_equals
else:
    op = math_ops.tensor_not_equals
x = constant_op.constant(4)
try:
    result = op(x, float_literal)
    if isinstance(result, ops.Tensor):
        result = self.evaluate(result)
except TypeError:
    # Throwing a TypeError is OK
    exit()
self.assertEqual(result, not is_equals)
