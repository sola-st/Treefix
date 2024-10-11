# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Test the case where there are no predictions and labels for
# one class, and thus there is one row and one column with
# zero entries in the confusion matrix.
num_classes = 3
with self.cached_session() as sess:
    # Create the queue that populates the predictions.
    # There is no prediction for class 2.
    preds_queue = data_flow_ops.FIFOQueue(
        5, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [0])
    predictions = preds_queue.dequeue()

    # Create the queue that populates the labels.
    # There is label for class 2.
    labels_queue = data_flow_ops.FIFOQueue(
        5, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    labels = labels_queue.dequeue()

    mean_accuracy, update_op = metrics.mean_per_class_accuracy(
        labels, predictions, num_classes)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(5):
        self.evaluate(update_op)
    desired_output = np.mean([1.0 / 2.0, 2.0 / 3.0, 0.])
    self.assertAlmostEqual(desired_output, self.evaluate(mean_accuracy))
