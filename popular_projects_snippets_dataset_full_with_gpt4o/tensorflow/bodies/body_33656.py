# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = random_ops.random_uniform(
    (10, 3), maxval=3, dtype=dtypes_lib.int64, seed=1)
labels = random_ops.random_uniform(
    (10, 3), maxval=3, dtype=dtypes_lib.int64, seed=1)
accuracy, update_op = metrics.accuracy(labels, predictions)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates.
    for _ in range(10):
        self.evaluate(update_op)

    # Then verify idempotency.
    initial_accuracy = self.evaluate(accuracy)
    for _ in range(10):
        self.assertEqual(initial_accuracy, self.evaluate(accuracy))
