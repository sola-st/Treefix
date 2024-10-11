# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
inputs = np.random.randint(0, 2, size=(100, 1))

predictions = constant_op.constant(inputs, dtype=dtypes_lib.float32)
labels = constant_op.constant(inputs)
specificity, update_op = metrics.specificity_at_sensitivity(
    labels, predictions, sensitivity=0.7)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(1, self.evaluate(update_op))
    self.assertEqual(1, self.evaluate(specificity))
