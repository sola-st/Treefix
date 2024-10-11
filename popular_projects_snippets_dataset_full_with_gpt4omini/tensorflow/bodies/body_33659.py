# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.ones((40, 1))
labels = array_ops.ones((40,))
with self.cached_session():
    accuracy, update_op = metrics.accuracy(labels, predictions, weights=2.0)

    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(1.0, self.evaluate(update_op))
    self.assertEqual(1.0, self.evaluate(accuracy))
