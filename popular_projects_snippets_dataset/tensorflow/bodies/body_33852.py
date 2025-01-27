# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
num_classes = 3
predictions = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)
labels = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)
mean_accuracy, update_op = metrics.mean_per_class_accuracy(
    labels, predictions, num_classes=num_classes)

with self.cached_session():
    self.evaluate(variables.local_variables_initializer())

    # Run several updates.
    for _ in range(10):
        self.evaluate(update_op)

    # Then verify idempotency.
    initial_mean_accuracy = self.evaluate(mean_accuracy)
    for _ in range(10):
        self.assertEqual(initial_mean_accuracy, self.evaluate(mean_accuracy))

num_classes = 3
with self.cached_session() as sess:
    # Create the queue that populates the predictions.
    preds_queue = data_flow_ops.FIFOQueue(
        5, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [2])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [0])
    predictions = preds_queue.dequeue()

    # Create the queue that populates the labels.
    labels_queue = data_flow_ops.FIFOQueue(
        5, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [2])
    _enqueue_vector(sess, labels_queue, [1])
    labels = labels_queue.dequeue()

    mean_accuracy, update_op = metrics.mean_per_class_accuracy(
        labels, predictions, num_classes)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(5):
        self.evaluate(update_op)
    desired_output = np.mean([1.0, 1.0 / 3.0, 0.0])
    self.assertAlmostEqual(desired_output, self.evaluate(mean_accuracy))
