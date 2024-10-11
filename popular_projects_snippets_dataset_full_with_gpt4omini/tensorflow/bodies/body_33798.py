# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.zeros((1, 3), dtype=dtypes_lib.float32)
labels = array_ops.zeros((1, 3), dtype=dtypes_lib.float32)

error, update_op = metrics.mean_squared_error(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(0, self.evaluate(update_op))
    self.assertEqual(0, self.evaluate(error))
