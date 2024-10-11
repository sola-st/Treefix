# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
inputs = np.random.randint(0, 2, size=(100, 1))

with self.cached_session():
    predictions = constant_op.constant(inputs, dtype=dtypes_lib.float32)
    labels = constant_op.constant(inputs)
    auc, update_op = metrics.auc(labels, predictions, curve=curve)

    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(1, self.evaluate(update_op))

    self.assertEqual(1, self.evaluate(auc))
