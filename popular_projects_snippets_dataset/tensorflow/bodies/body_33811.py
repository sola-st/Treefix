# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        [2, 4, 6, 8], shape=(1, 4), dtype=dtypes_lib.float32)
    labels = constant_op.constant(
        [1, 3, 2, 3], shape=(1, 4), dtype=dtypes_lib.float32)
    weights = constant_op.constant([0, 1, 0, 1], shape=(1, 4))

    rmse, update_op = metrics.root_mean_squared_error(labels, predictions,
                                                      weights)

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(math.sqrt(13), self.evaluate(update_op))

    self.assertAlmostEqual(math.sqrt(13), self.evaluate(rmse), 5)
