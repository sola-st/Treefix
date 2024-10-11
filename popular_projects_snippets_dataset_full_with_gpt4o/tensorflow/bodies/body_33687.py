# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.zeros((1, 4))
labels = array_ops.zeros((1, 4))
recall, update_op = metrics.recall(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.evaluate(update_op)
    self.assertEqual(0, self.evaluate(recall))
