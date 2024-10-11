# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    # Create the queue that populates one set of predictions.
    preds_queue0 = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, preds_queue0, [10, 8, 6])
    _enqueue_vector(sess, preds_queue0, [-4, 3, -1])
    predictions0 = preds_queue0.dequeue()

    # Create the queue that populates one set of predictions.
    preds_queue1 = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, preds_queue1, [0, 1, 1])
    _enqueue_vector(sess, preds_queue1, [1, 1, 0])
    predictions1 = preds_queue1.dequeue()

    # Create the queue that populates one set of labels.
    labels_queue0 = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, labels_queue0, [1, 3, 2])
    _enqueue_vector(sess, labels_queue0, [2, 4, 6])
    labels0 = labels_queue0.dequeue()

    # Create the queue that populates another set of labels.
    labels_queue1 = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(1, 3))
    _enqueue_vector(sess, labels_queue1, [-5, -3, -1])
    _enqueue_vector(sess, labels_queue1, [5, 4, 3])
    labels1 = labels_queue1.dequeue()

    mse0, update_op0 = metrics.mean_squared_error(
        labels0, predictions0, name='msd0')
    mse1, update_op1 = metrics.mean_squared_error(
        labels1, predictions1, name='msd1')

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([update_op0, update_op1])
    self.evaluate([update_op0, update_op1])

    mse0, mse1 = self.evaluate([mse0, mse1])
    self.assertAlmostEqual(208.0 / 6, mse0, 5)
    self.assertAlmostEqual(79.0 / 6, mse1, 5)
