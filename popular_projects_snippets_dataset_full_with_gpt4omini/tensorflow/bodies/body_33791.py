# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
np_predictions = np.asarray([2, 4, 6, 8], dtype=np.float32)
np_labels = np.asarray([1, 3, 2, 3], dtype=np.float32)
expected_error = np.mean(
    np.divide(np.absolute(np_predictions - np_labels), np_labels))

predictions = constant_op.constant(
    np_predictions, shape=(1, 4), dtype=dtypes_lib.float32)
labels = constant_op.constant(np_labels, shape=(1, 4))

error, update_op = metrics.mean_relative_error(
    labels, predictions, normalizer=labels)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(expected_error, self.evaluate(update_op))
    self.assertEqual(expected_error, self.evaluate(error))
