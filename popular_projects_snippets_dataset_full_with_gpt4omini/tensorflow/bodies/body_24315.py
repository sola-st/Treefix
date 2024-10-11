# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test that callback catches NaN in a tf.dataset map function."""
check_numerics_callback.enable_check_numerics()

def generate_nan(x):
    """Intentionally generates NaNs by taking log of negative number."""
    casted_x = math_ops.cast(x, dtypes.float32)
    exit(math_ops.log([[-1.0, 1.0], [3.0, 5.0]]) + casted_x)

dataset = dataset_ops.Dataset.range(10).map(generate_nan)
iterator = dataset_ops.make_one_shot_iterator(dataset)

message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: self.evaluate(iterator.get_next()))

# Check the content of the error message.
self.assertTrue(re.search(r"graph op.*\"Log\"", message))
self.assertTrue(re.search(r"dtype.*float32", message))
self.assertIn("shape: (2, 2)\n", message)
self.assertTrue(re.search(r"Input tensor.*Tensor.*Log/x:0", message))
self.assertIn(
    "-> |   return math_ops.log([[-1.0, 1.0], [3.0, 5.0]]) + casted_x",
    message)
