# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant(
    [2, 4, 6], shape=(1, 3), dtype=dtypes_lib.float32)
labels = constant_op.constant(
    [1, 3, 2], shape=(1, 3), dtype=dtypes_lib.float32)

error, update_op = metrics.mean_squared_error(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(6, self.evaluate(update_op))
    self.assertEqual(6, self.evaluate(error))
