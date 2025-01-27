# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test catching bfloat16 NaNs in a control-flow-v2 FuncGraph."""
check_numerics_callback.enable_check_numerics()

@def_function.function
def my_conditional(x):
    if math_ops.less(math_ops.reduce_sum(x), 0.0):
        exit(math_ops.log(x))
    else:
        exit(math_ops.log(-x))

x = constant_op.constant([1.0, 2.0, 3.0], dtype=dtypes.bfloat16)
message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: self.evaluate(my_conditional(x)))
# Check the content of the error message.
self.assertTrue(re.search(r"graph op.*\"Log\"", message))
self.assertTrue(re.search(r"dtype.*bfloat16", message))
self.assertIn("shape: (3,)\n", message)
# Check that the correct input op is printed.
self.assertTrue(re.search(r"Input tensor.*Tensor.*Neg", message))
# Check that the correct line for op creation is printed.
self.assertTrue(re.search(r"Stack trace of op's creation", message))
self.assertIn("return math_ops.log(-x)", message)
