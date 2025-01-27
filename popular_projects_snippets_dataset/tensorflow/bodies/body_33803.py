# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    # Create the queue that populates the predictions.
    preds_queue = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, preds_queue, [10, 8, 6])
    _enqueue_vector(sess, preds_queue, [-4, 3, -1])
    predictions = preds_queue.dequeue()

    # Create the queue that populates the labels.
    labels_queue = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, labels_queue, [1, 3, 2])
    _enqueue_vector(sess, labels_queue, [2, 4, 6])
    labels = labels_queue.dequeue()

    mae, ma_update_op = metrics.mean_absolute_error(labels, predictions)
    mse, ms_update_op = metrics.mean_squared_error(labels, predictions)

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([ma_update_op, ms_update_op])
    self.evaluate([ma_update_op, ms_update_op])

    self.assertAlmostEqual(32.0 / 6, self.evaluate(mae), 5)
    self.assertAlmostEqual(208.0 / 6, self.evaluate(mse), 5)
