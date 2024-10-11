# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = random_ops.random_normal((10, 3), seed=1)
labels = random_ops.random_normal((10, 3), seed=2)
error, update_op = metrics.mean_squared_error(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates.
    for _ in range(10):
        self.evaluate(update_op)

    # Then verify idempotency.
    initial_error = self.evaluate(error)
    for _ in range(10):
        self.assertEqual(initial_error, self.evaluate(error))
