# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant([[1, 0, 1, 0], [0, 1, 0, 1]])
labels = constant_op.constant([[0, 1, 1, 0], [1, 0, 0, 1]])
weights = constant_op.constant([[1, 2, 3, 4], [4, 3, 2, 1]])
recall, update_op = metrics.recall(labels, predictions, weights=weights)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    weighted_tp = 3.0 + 1.0
    weighted_t = (2.0 + 3.0) + (4.0 + 1.0)
    expected_precision = weighted_tp / weighted_t
    self.assertAlmostEqual(expected_precision, self.evaluate(update_op))
    self.assertAlmostEqual(expected_precision, self.evaluate(recall))
