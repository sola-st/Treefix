# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = array_ops.zeros([4], dtype=dtypes_lib.float32)
    labels = array_ops.zeros([4])
    auc, update_op = metrics.auc(labels, predictions)

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(1, self.evaluate(update_op), 6)

    self.assertAlmostEqual(1, self.evaluate(auc), 6)
