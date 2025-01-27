# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    # Create the queue that populates the values.
    values_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 2))
    _enqueue_vector(sess, values_queue, [0, 1])
    _enqueue_vector(sess, values_queue, [-4.2, 9.1])
    _enqueue_vector(sess, values_queue, [6.5, 0])
    _enqueue_vector(sess, values_queue, [-3.2, 4.0])
    values = values_queue.dequeue()

    # Create the queue that populates the weights.
    weights_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 1))
    _enqueue_vector(sess, weights_queue, [[0.0025]])
    _enqueue_vector(sess, weights_queue, [[0.005]])
    _enqueue_vector(sess, weights_queue, [[0.01]])
    _enqueue_vector(sess, weights_queue, [[0.0075]])
    weights = weights_queue.dequeue()

    mean, update_op = metrics.mean_tensor(values, weights)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(4):
        self.evaluate(update_op)
    self.assertAllClose([[0.8, 3.52]], self.evaluate(mean), 5)
