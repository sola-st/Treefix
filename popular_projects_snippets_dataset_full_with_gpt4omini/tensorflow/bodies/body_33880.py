# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant(((0.9, 0.2, 0.8, 0.1),
                                    (0.2, 0.9, 0.7, 0.6),
                                    (0.1, 0.2, 0.4, 0.3)))
labels = constant_op.constant(((0, 1, 1, 0),
                               (1, 0, 0, 0),
                               (0, 0, 0, 0)))
tn, tn_update_op = metrics.true_negatives_at_thresholds(
    predictions=predictions, labels=labels, thresholds=[0.15, 0.5, 0.85])

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual((0, 0, 0), tn)
    self.assertAllEqual((2, 5, 7), tn_update_op)
    self.assertAllEqual((2, 5, 7), tn)
