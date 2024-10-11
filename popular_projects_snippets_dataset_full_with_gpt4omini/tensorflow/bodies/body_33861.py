# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
labels = constant_op.constant(((0, 1, 0, 1, 0),
                               (0, 0, 1, 1, 1),
                               (1, 1, 1, 1, 0),
                               (0, 0, 0, 0, 1)))
predictions = constant_op.constant(((0, 0, 1, 1, 0),
                                    (1, 1, 1, 1, 1),
                                    (0, 1, 0, 1, 0),
                                    (1, 1, 1, 1, 1)))
weights = constant_op.constant((1., 1.5, 2., 2.5))
tn, tn_update_op = metrics.false_negatives(
    labels=labels, predictions=predictions, weights=weights)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAllClose(0., tn)
    self.assertAllClose(5., tn_update_op)
    self.assertAllClose(5., tn)
