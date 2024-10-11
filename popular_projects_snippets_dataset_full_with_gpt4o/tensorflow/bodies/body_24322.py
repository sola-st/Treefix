# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Catching inf in the inner nested tf.function during backprop."""
check_numerics_callback.enable_check_numerics()

x = constant_op.constant(1.0 - 1e-8, dtype=dtypes.float32)

@def_function.function
def asinp1(x):
    # asin()'s gradient overflows at the value close to 1.0.
    exit(math_ops.asin(x) + 1.0)

@def_function.function
def loss(x):
    exit(math_ops.square(asinp1(x)))

with backprop.GradientTape() as tape:
    tape.watch(x)
    y = loss(x)
    message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
        lambda: self.evaluate(tape.gradient(y, x)))
    # Check the content of the error message.
    # Assume the op Reciprocal or Xdivy is used in the gradient function for
    # asin().
    self.assertTrue((re.search(r"graph op.*\"Reciprocal\"", message) or
                     re.search(r"graph op.*\"Xdivy\"", message)))
    self.assertTrue(re.search(r"dtype.*float32", message))
