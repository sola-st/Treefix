# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
num_classes = 2
with self.cached_session() as sess:
    # Create the queue that populates the predictions.
    preds_queue = data_flow_ops.FIFOQueue(
        6, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    _enqueue_vector(sess, preds_queue, [0])
    _enqueue_vector(sess, preds_queue, [1])
    predictions = preds_queue.dequeue()

    # Create the queue that populates the labels.
    labels_queue = data_flow_ops.FIFOQueue(
        6, dtypes=dtypes_lib.int32, shapes=(1, 1))
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [1])
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [0])
    _enqueue_vector(sess, labels_queue, [1])
    labels = labels_queue.dequeue()

    # Create the queue that populates the weights.
    weights_queue = data_flow_ops.FIFOQueue(
        6, dtypes=dtypes_lib.float32, shapes=(1, 1))
    _enqueue_vector(sess, weights_queue, [1.0])
    _enqueue_vector(sess, weights_queue, [1.0])
    _enqueue_vector(sess, weights_queue, [1.0])
    _enqueue_vector(sess, weights_queue, [0.0])
    _enqueue_vector(sess, weights_queue, [1.0])
    _enqueue_vector(sess, weights_queue, [0.0])
    weights = weights_queue.dequeue()

    mean_iou, update_op = metrics.mean_iou(
        labels, predictions, num_classes, weights=weights)

    variables.local_variables_initializer().run()
    for _ in range(6):
        self.evaluate(update_op)
    desired_output = np.mean([2.0 / 3.0, 1.0 / 2.0])
    self.assertAlmostEqual(desired_output, self.evaluate(mean_iou))
