# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
np_predictions = np.matrix(
    ('0.819031913261206 0.567041924552012 0.087465312324590;'
     '-0.665139432070255 -0.739487441769973 -0.103671883216994;'
     '0.707106781186548 -0.707106781186548 0'))
np_labels = np.matrix(
    ('0.819031913261206 0.567041924552012 0.087465312324590;'
     '0.665139432070255 0.739487441769973 0.103671883216994;'
     '0.707106781186548 0.707106781186548 0'))

predictions = constant_op.constant(
    np_predictions, shape=(3, 1, 3), dtype=dtypes_lib.float32)
labels = constant_op.constant(
    np_labels, shape=(3, 1, 3), dtype=dtypes_lib.float32)
error, update_op = metrics.mean_cosine_distance(labels, predictions, dim=2)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(1.0, self.evaluate(update_op), 5)
    self.assertAlmostEqual(1.0, self.evaluate(error), 5)
