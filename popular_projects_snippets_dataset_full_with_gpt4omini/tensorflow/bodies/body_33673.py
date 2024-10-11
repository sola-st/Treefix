# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant([[1, 0, 1, 0], [1, 0, 1, 0]])
labels = constant_op.constant([[0, 1, 1, 0], [1, 0, 0, 1]])
precision, update_op = metrics.precision(
    labels,
    predictions,
    weights=constant_op.constant([[1, 2, 3, 4], [4, 3, 2, 1]]))

with self.cached_session():
    variables.local_variables_initializer().run()
    weighted_tp = 3.0 + 4.0
    weighted_positives = (1.0 + 3.0) + (4.0 + 2.0)
    expected_precision = weighted_tp / weighted_positives
    self.assertAlmostEqual(expected_precision, self.evaluate(update_op))
    self.assertAlmostEqual(expected_precision, self.evaluate(precision))
