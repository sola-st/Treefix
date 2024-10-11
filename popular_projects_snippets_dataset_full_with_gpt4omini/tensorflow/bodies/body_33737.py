# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
inputs = np.random.randint(0, 2, size=(100, 1))

with self.cached_session():
    predictions = constant_op.constant(inputs, dtype=dtypes_lib.float32)
    labels = constant_op.constant(1 - inputs, dtype=dtypes_lib.float32)
    thresholds = [0.5]
    prec, prec_op = metrics.precision_at_thresholds(labels, predictions,
                                                    thresholds)
    rec, rec_op = metrics.recall_at_thresholds(labels, predictions,
                                               thresholds)

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([prec_op, rec_op])

    self.assertAlmostEqual(0, self.evaluate(prec))
    self.assertAlmostEqual(0, self.evaluate(rec))
