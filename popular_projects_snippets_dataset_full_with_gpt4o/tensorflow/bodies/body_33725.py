# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = random_ops.random_uniform(
    (10, 3), maxval=1, dtype=dtypes_lib.float32, seed=1)
labels = random_ops.random_uniform(
    (10, 3), maxval=2, dtype=dtypes_lib.int64, seed=1)
sensitivity, update_op = metrics.sensitivity_at_specificity(
    labels, predictions, specificity=0.7)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates.
    for _ in range(10):
        self.evaluate(update_op)

    # Then verify idempotency.
    initial_sensitivity = self.evaluate(sensitivity)
    for _ in range(10):
        self.assertAlmostEqual(initial_sensitivity, self.evaluate(sensitivity),
                               5)
