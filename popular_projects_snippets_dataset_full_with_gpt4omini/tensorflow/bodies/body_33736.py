# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    for label_dtype in (
        dtypes_lib.bool, dtypes_lib.int32, dtypes_lib.float32):
        predictions = constant_op.constant(
            [1, 0, 1, 0], shape=(1, 4), dtype=dtypes_lib.float32)
        labels = math_ops.cast(
            constant_op.constant([0, 1, 1, 0], shape=(1, 4)), dtype=label_dtype)
        thresholds = [0.5]
        prec, prec_op = metrics.precision_at_thresholds(labels, predictions,
                                                        thresholds)
        rec, rec_op = metrics.recall_at_thresholds(labels, predictions,
                                                   thresholds)

        self.evaluate(variables.local_variables_initializer())
        self.evaluate([prec_op, rec_op])

        self.assertAlmostEqual(0.5, self.evaluate(prec))
        self.assertAlmostEqual(0.5, self.evaluate(rec))
