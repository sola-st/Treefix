# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
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

    miou, update_op = metrics.mean_iou(labels, predictions, num_classes)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(5):
        self.evaluate(update_op)
    desired_output = np.mean([1.0 / 2.0, 1.0 / 4.0, 0.])
    self.assertEqual(desired_output, self.evaluate(miou))
