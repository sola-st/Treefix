# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.placeholder(dtype=dtypes_lib.float32)
labels = array_ops.placeholder(dtype=dtypes_lib.float32)
feed_dict = {
    predictions: ((1, 0, 1, 0), (1, 0, 1, 0)),
    labels: ((0, 1, 1, 0), (1, 0, 0, 1))
}
precision, update_op = metrics.precision(
    labels, predictions, weights=constant_op.constant([[2], [5]]))

with self.cached_session():
    variables.local_variables_initializer().run()
    weighted_tp = 2.0 + 5.0
    weighted_positives = (2.0 + 2.0) + (5.0 + 5.0)
    expected_precision = weighted_tp / weighted_positives
    self.assertAlmostEqual(
        expected_precision, update_op.eval(feed_dict=feed_dict))
    self.assertAlmostEqual(
        expected_precision, precision.eval(feed_dict=feed_dict))
