# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session() as sess:
    values_queue = data_flow_ops.FIFOQueue(
        2, dtypes=dtypes_lib.float32, shapes=(2, 2, 2))
    _enqueue_vector(
        sess,
        values_queue, [[[1, 2], [1, 2]], [[1, 2], [1, 2]]],
        shape=(2, 2, 2))
    _enqueue_vector(
        sess,
        values_queue, [[[1, 2], [1, 2]], [[3, 4], [9, 10]]],
        shape=(2, 2, 2))
    values = values_queue.dequeue()

    mean, update_op = metrics.mean_tensor(values)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(2):
        self.evaluate(update_op)
    self.assertAllClose([[[1, 2], [1, 2]], [[2, 3], [5, 6]]],
                        self.evaluate(mean))
