# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
inputs = np.random.randint(0, 2, size=(100, 1))

predictions = constant_op.constant(inputs)
labels = constant_op.constant(inputs)
precision, update_op = metrics.precision(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(1.0, self.evaluate(update_op), 6)
    self.assertAlmostEqual(1.0, self.evaluate(precision), 6)
