# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    values_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 2))
    _enqueue_vector(sess, values_queue, [0, 1])
    _enqueue_vector(sess, values_queue, [-4.2, 9.1])
    _enqueue_vector(sess, values_queue, [6.5, 0])
    _enqueue_vector(sess, values_queue, [-3.2, 4.0])
    values = values_queue.dequeue()

    mean, update_op = metrics.mean(values)

    self.evaluate(variables.local_variables_initializer())

    self.assertAlmostEqual(0.5, self.evaluate(update_op), 5)
    self.assertAlmostEqual(1.475, self.evaluate(update_op), 5)
    self.assertAlmostEqual(12.4 / 6.0, self.evaluate(update_op), 5)
    self.assertAlmostEqual(1.65, self.evaluate(update_op), 5)

    self.assertAlmostEqual(1.65, self.evaluate(mean), 5)
