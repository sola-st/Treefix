# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant([0, 0, 0, 0])
labels = constant_op.constant([0, 0, 0, 0])
precision, update_op = metrics.precision(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.evaluate(update_op)
    self.assertEqual(0.0, self.evaluate(precision))
