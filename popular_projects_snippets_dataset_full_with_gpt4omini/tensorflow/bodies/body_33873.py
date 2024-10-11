# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = constant_op.constant(((0.9, 0.2, 0.8, 0.1),
                                    (0.2, 0.9, 0.7, 0.6),
                                    (0.1, 0.2, 0.4, 0.3)))
labels = constant_op.constant(((0, 1, 1, 0),
                               (1, 0, 0, 0),
                               (0, 0, 0, 0)))
fp, fp_update_op = metrics.false_positives_at_thresholds(
    predictions=predictions,
    labels=labels,
    weights=((1.0, 2.0, 3.0, 5.0),
             (7.0, 11.0, 13.0, 17.0),
             (19.0, 23.0, 29.0, 31.0)),
    thresholds=[0.15, 0.5, 0.85])

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual((0.0, 0.0, 0.0), fp)
    self.assertAllEqual((125.0, 42.0, 12.0), fp_update_op)
    self.assertAllEqual((125.0, 42.0, 12.0), fp)
