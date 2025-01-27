# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    predictions = constant_op.constant(
        0.0, shape=(1, 3), dtype=dtypes_lib.float32)
    labels = constant_op.constant(0.0, shape=(1, 3), dtype=dtypes_lib.float32)

    rmse, update_op = metrics.root_mean_squared_error(labels, predictions)

    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(0, self.evaluate(update_op))

    self.assertEqual(0, self.evaluate(rmse))
