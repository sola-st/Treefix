# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
inputs = np.random.randint(0, 2, size=(100, 1))

with self.cached_session():
    predictions = constant_op.constant(inputs, dtype=dtypes_lib.float32)
    labels = constant_op.constant(1 - inputs, dtype=dtypes_lib.float32)
    auc, update_op = metrics.auc(labels, predictions)

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(0, self.evaluate(update_op))

    self.assertAlmostEqual(0, self.evaluate(auc))
