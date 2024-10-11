# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
np_inputs = np.random.randint(0, 2, size=(100, 1))

predictions = constant_op.constant(np_inputs)
labels = constant_op.constant(np_inputs)
recall, update_op = metrics.recall(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.evaluate(update_op)
    self.assertAlmostEqual(1.0, self.evaluate(recall), 6)
