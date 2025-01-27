# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
num_classes = 3
predictions = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)
labels = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)
mean_iou, update_op = metrics.mean_iou(
    labels, predictions, num_classes=num_classes)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates.
    for _ in range(10):
        self.evaluate(update_op)

    # Then verify idempotency.
    initial_mean_iou = self.evaluate(mean_iou)
    for _ in range(10):
        self.assertEqual(initial_mean_iou, self.evaluate(mean_iou))
