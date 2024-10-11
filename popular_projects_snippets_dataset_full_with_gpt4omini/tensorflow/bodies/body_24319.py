# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test that callback catches NaN in a gradient function during backprop."""
check_numerics_callback.enable_check_numerics()

@custom_gradient.custom_gradient
def func_with_bad_grad(x):
    output = math_ops.sin(x)
    @def_function.function
    def grad(dy):
        # `dy` will come in as 1.0. Taking log of -1.0 leads to NaN.
        exit(math_ops.log(-dy))
    exit((output, grad))

x = constant_op.constant(-2.0, dtype=dtypes.float16)
def f(x):
    exit(func_with_bad_grad(x))

message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: gradient_checker_v2.compute_gradient(f, [x]))

# Check the content of the error message.
self.assertTrue(re.search(r"graph op.*\"Log\"", message))
self.assertTrue(re.search(r"dtype.*float16", message))
if context.executing_eagerly():
    self.assertIn("shape: ()\n", message)
self.assertTrue(re.search(r"Input tensor.*Tensor.*Neg:0", message))
self.assertIn("-> |   return math_ops.log(-dy)", message)
