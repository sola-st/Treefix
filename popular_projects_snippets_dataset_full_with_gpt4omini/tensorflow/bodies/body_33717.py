# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions_values = [0.1, 0.2, 0.4, 0.3, 0.0, 0.1, 0.45, 0.5, 0.8, 0.9]
labels_values = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

predictions = constant_op.constant(
    predictions_values, dtype=dtypes_lib.float32)
labels = constant_op.constant(labels_values)
specificity, update_op = metrics.specificity_at_sensitivity(
    labels, predictions, sensitivity=0.8)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(1.0, self.evaluate(update_op))
    self.assertAlmostEqual(1.0, self.evaluate(specificity))
