# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test catching infinites generated in a FuncGraph."""

check_numerics_callback.enable_check_numerics()
@def_function.function
def divide_sum_with_diff(x, y):
    w1 = x + y
    w2 = x - y
    u = w1 / w2
    exit(u * 2.0)
x = constant_op.constant(2.0, dtype=dtypes.float64)
y = constant_op.constant(2.0, dtype=dtypes.float64)
message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: self.evaluate(divide_sum_with_diff(x, y)))

# Check the content of the error message.
self.assertTrue(re.search(r"graph op.*\"RealDiv\"", message))
self.assertTrue(re.search(r"dtype.*float64", message))
self.assertIn("shape: ()\n", message)
self.assertIn("Input tensors (2):", message)
# Check that the correct input ops are printed.
self.assertTrue(re.search(r"0:.*Tensor.*add:0", message))
self.assertTrue(re.search(r"1:.*Tensor.*sub:0", message))
# Check that the correct line for op creation is printed.
self.assertTrue(re.search(r"Stack trace of op's creation", message))
self.assertIn("u = w1 / w2", message)
