# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [[1, 0], [1, 0]], shape=(2, 2), dtype=dtypes_lib.float32)
    labels = constant_op.constant([[0, 1], [1, 0]], shape=(2, 2))
    weights = constant_op.constant(
        [[0], [1]], shape=(2, 1), dtype=dtypes_lib.float32)
    thresholds = [0.5, 1.1]
    prec, prec_op = metrics.precision_at_thresholds(
        labels, predictions, thresholds, weights=weights)
    rec, rec_op = metrics.recall_at_thresholds(
        labels, predictions, thresholds, weights=weights)

    [prec_low, prec_high] = array_ops.split(
        value=prec, num_or_size_splits=2, axis=0)
    prec_low = array_ops.reshape(prec_low, shape=())
    prec_high = array_ops.reshape(prec_high, shape=())
    [rec_low, rec_high] = array_ops.split(
        value=rec, num_or_size_splits=2, axis=0)
    rec_low = array_ops.reshape(rec_low, shape=())
    rec_high = array_ops.reshape(rec_high, shape=())

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([prec_op, rec_op])

    self.assertAlmostEqual(1.0, self.evaluate(prec_low), places=5)
    self.assertAlmostEqual(0.0, self.evaluate(prec_high), places=5)
    self.assertAlmostEqual(1.0, self.evaluate(rec_low), places=5)
    self.assertAlmostEqual(0.0, self.evaluate(rec_high), places=5)
