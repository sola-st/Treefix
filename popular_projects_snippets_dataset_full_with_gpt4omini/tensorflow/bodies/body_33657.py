# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    # Create the queue that populates the predictions.
    preds_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 1))
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [2])
    _enqueue_vector(sess, preds_queue, [1])
    predictions = preds_queue.dequeue()

    # Create the queue that populates the labels.
    labels_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 1))
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [2])
    labels = labels_queue.dequeue()

    accuracy, update_op = metrics.accuracy(labels, predictions)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(3):
        self.evaluate(update_op)
    self.assertEqual(0.5, self.evaluate(update_op))
    self.assertEqual(0.5, self.evaluate(accuracy))
