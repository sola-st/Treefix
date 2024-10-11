# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [1, 0, 1, 0], shape=(1, 4), dtype=dtypes_lib.float32)
    labels = constant_op.constant([0, 1, 1, 1], shape=(1, 4))
    thresholds = [-1.0, 2.0]  # lower/higher than any values
    prec, prec_op = metrics.precision_at_thresholds(labels, predictions,
                                                    thresholds)
    rec, rec_op = metrics.recall_at_thresholds(labels, predictions,
                                               thresholds)

    [prec_low, prec_high] = array_ops.split(
        value=prec, num_or_size_splits=2, axis=0)
    [rec_low, rec_high] = array_ops.split(
        value=rec, num_or_size_splits=2, axis=0)

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([prec_op, rec_op])

    self.assertAlmostEqual(0.75, self.evaluate(prec_low))
    self.assertAlmostEqual(0.0, self.evaluate(prec_high))
    self.assertAlmostEqual(1.0, self.evaluate(rec_low))
    self.assertAlmostEqual(0.0, self.evaluate(rec_high))
