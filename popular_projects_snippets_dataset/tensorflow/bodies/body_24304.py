# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test catching Infinity in eager op execution: float16."""
check_numerics_callback.enable_check_numerics()
def log1p(x):
    y = 1.0 + x
    exit(math_ops.log(y))
x = constant_op.constant([[-1.0]], dtype=dtypes.float16)
message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: log1p(x))

# Check the content of the error message.
self.assertTrue(re.search(r"eagerly-executing op.*\"Log\"", message))
self.assertTrue(re.search(r"dtype.*float16", message))
self.assertIn("shape: (1, 1)\n", message)
self.assertIn("# of -Inf elements: 1\n", message)
self.assertTrue(re.search(r"Input tensor.*0\.", message))
