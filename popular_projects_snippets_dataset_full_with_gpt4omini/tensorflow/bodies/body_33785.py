# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant(
    [2, 4, 6, 8], shape=(1, 4), dtype=dtypes_lib.float32)
labels = constant_op.constant(
    [1, 3, 2, 3], shape=(1, 4), dtype=dtypes_lib.float32)
weights = constant_op.constant([0, 1, 0, 1], shape=(1, 4))

error, update_op = metrics.mean_absolute_error(labels, predictions, weights)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(3, self.evaluate(update_op))
    self.assertEqual(3, self.evaluate(error))
