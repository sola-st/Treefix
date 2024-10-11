# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant(((0.9, 0.2, 0.8, 0.1),
                                    (0.2, 0.9, 0.7, 0.6),
                                    (0.1, 0.2, 0.4, 0.3)))
labels = constant_op.constant(((0, 1, 1, 0),
                               (1, 0, 0, 0),
                               (0, 0, 0, 0)))
tp, tp_update_op = metrics.true_positives_at_thresholds(
    predictions=predictions, labels=labels, weights=37.0,
    thresholds=[0.15, 0.5, 0.85])

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual((0.0, 0.0, 0.0), tp)
    self.assertAllEqual((111.0, 37.0, 0.0), tp_update_op)
    self.assertAllEqual((111.0, 37.0, 0.0), tp)
