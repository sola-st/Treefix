# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions_values = [0.1, 0.2, 0.4, 0.3, 0.0, 0.1, 0.2, 0.2, 0.26, 0.26]
labels_values = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
weights_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

predictions = constant_op.constant(
    predictions_values, dtype=dtypes_lib.float32)
labels = constant_op.constant(labels_values)
weights = constant_op.constant(weights_values)
specificity, update_op = metrics.specificity_at_sensitivity(
    labels, predictions, weights=weights, sensitivity=0.4)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    self.assertAlmostEqual(8.0 / 15.0, self.evaluate(update_op))
    self.assertAlmostEqual(8.0 / 15.0, self.evaluate(specificity))
