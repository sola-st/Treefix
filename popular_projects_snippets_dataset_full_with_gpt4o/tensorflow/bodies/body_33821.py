# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
np_predictions = np.matrix(('1 0 0;' '0 0 -1;' '1 0 0'))
np_labels = np.matrix(('1 0 0;' '0 0 1;' '0 1 0'))

predictions = constant_op.constant(
    np_predictions, shape=(3, 1, 3), dtype=dtypes_lib.float32)
labels = constant_op.constant(
    np_labels, shape=(3, 1, 3), dtype=dtypes_lib.float32)
weights = constant_op.constant(
    [1, 0, 0], shape=(3, 1, 1), dtype=dtypes_lib.float32)

error, update_op = metrics.mean_cosine_distance(
    labels, predictions, dim=2, weights=weights)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(0, self.evaluate(update_op))
    self.assertEqual(0, self.evaluate(error))
