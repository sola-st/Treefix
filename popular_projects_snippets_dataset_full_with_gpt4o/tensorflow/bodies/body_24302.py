# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Two calls to enable_check_numerics() have same effect as one call."""
check_numerics_callback.enable_check_numerics()
check_numerics_callback.enable_check_numerics()

x = constant_op.constant([2.0, 3.0])
y = constant_op.constant([1.0, 0.0])
message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: x / y)

# Check the content of the error message.
self.assertTrue(re.search(r"eagerly-executing op.*\"RealDiv\"", message))
self.assertTrue(re.search(r"dtype.*float32", message))
self.assertIn("shape: (2,)\n", message)
self.assertIn("# of +Inf elements: 1\n", message)
self.assertIn("0: %s" % x, message)
self.assertIn("1: %s" % y, message)
