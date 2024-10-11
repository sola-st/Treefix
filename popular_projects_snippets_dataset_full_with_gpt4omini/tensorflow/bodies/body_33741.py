# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = array_ops.zeros([4], dtype=dtypes_lib.float32)
    labels = array_ops.zeros([4])
    thresholds = [0.5]
    prec, prec_op = metrics.precision_at_thresholds(labels, predictions,
                                                    thresholds)
    rec, rec_op = metrics.recall_at_thresholds(labels, predictions,
                                               thresholds)

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([prec_op, rec_op])

    self.assertAlmostEqual(0, self.evaluate(prec), 6)
    self.assertAlmostEqual(0, self.evaluate(rec), 6)
