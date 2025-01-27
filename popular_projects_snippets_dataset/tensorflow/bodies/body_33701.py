# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [0.0, 0.1, 0.2, 0.33, 0.3, 0.4, 0.5],
        shape=(1, 7),
        dtype=dtypes_lib.float32)
    labels = constant_op.constant([0, 0, 0, 0, 1, 1, 1], shape=(1, 7))
    auc, update_op = metrics.auc(labels, predictions, curve='PR',
                                 summation_method='careful_interpolation')

    self.evaluate(variables.local_variables_initializer())
    # expected ~= 0.90410597584
    expected = 1 - math.log(4./3) / 3
    self.assertAlmostEqual(expected, self.evaluate(update_op), delta=1e-3)
    self.assertAlmostEqual(expected, self.evaluate(auc), delta=1e-3)
