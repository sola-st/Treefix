# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
np_predictions = np.asarray([2, 4, 6, 8], dtype=np.float32)

predictions = constant_op.constant(
    np_predictions, shape=(1, 4), dtype=dtypes_lib.float32)
labels = constant_op.constant(
    [1, 3, 2, 3], shape=(1, 4), dtype=dtypes_lib.float32)

error, update_op = metrics.mean_relative_error(
    labels, predictions, normalizer=array_ops.zeros_like(labels))

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(0.0, self.evaluate(update_op))
    self.assertEqual(0.0, self.evaluate(error))
