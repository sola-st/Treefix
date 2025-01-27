# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [0.1, 0.4, 0.35, 0.8, 0.1, 0.135, 0.81],
        shape=(1, 7),
        dtype=dtypes_lib.float32)
    labels = constant_op.constant([0, 0, 1, 0, 1, 0, 1], shape=(1, 7))
    auc, update_op = metrics.auc(labels, predictions, curve='PR',
                                 summation_method='trapezoidal')

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(0.610317, self.evaluate(update_op), delta=1e-3)

    self.assertAlmostEqual(0.610317, self.evaluate(auc), delta=1e-3)
