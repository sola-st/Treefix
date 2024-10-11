# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [1, 0, 1, 0], shape=(1, 4), dtype=dtypes_lib.float32)
    labels = constant_op.constant([0, 1, 1, 0], shape=(1, 4))
    weights = constant_op.constant([1, 2, 3, 4], shape=(1, 4))
    auc, update_op = metrics.auc(labels, predictions, weights=weights)

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(0.7, self.evaluate(update_op), 5)

    self.assertAlmostEqual(0.7, self.evaluate(auc), 5)
