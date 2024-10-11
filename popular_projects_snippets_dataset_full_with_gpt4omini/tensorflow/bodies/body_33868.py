# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
labels = constant_op.constant(((0, 1, 0, 1, 0),
                               (0, 0, 1, 1, 1),
                               (1, 1, 1, 1, 0),
                               (0, 0, 0, 0, 1)))
predictions = constant_op.constant(((0, 0, 1, 1, 0),
                                    (1, 1, 1, 1, 1),
                                    (0, 1, 0, 1, 0),
                                    (1, 1, 1, 1, 1)))
tn, tn_update_op = metrics.false_positives(
    labels=labels, predictions=predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAllClose(0., tn)
    self.assertAllClose(7., tn_update_op)
    self.assertAllClose(7., tn)
