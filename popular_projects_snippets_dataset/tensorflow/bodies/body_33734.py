# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = random_ops.random_uniform(
    (10, 3), maxval=1, dtype=dtypes_lib.float32, seed=1)
labels = random_ops.random_uniform(
    (10, 3), maxval=1, dtype=dtypes_lib.int64, seed=1)
thresholds = [0, 0.5, 1.0]
prec, prec_op = metrics.precision_at_thresholds(labels, predictions,
                                                thresholds)
rec, rec_op = metrics.recall_at_thresholds(labels, predictions, thresholds)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates, then verify idempotency.
    self.evaluate([prec_op, rec_op])
    initial_prec = self.evaluate(prec)
    initial_rec = self.evaluate(rec)
    for _ in range(10):
        self.evaluate([prec_op, rec_op])
        self.assertAllClose(initial_prec, prec)
        self.assertAllClose(initial_rec, rec)
