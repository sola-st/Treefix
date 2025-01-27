# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(
        10, 5, [dtypes_lib.int32, dtypes_lib.int32], shapes=[(), (2,)])
    q.enqueue_many([[1, 2, 3, 4], [[1, 1], [2, 2], [3, 3], [4, 4]]]).run()
    self.assertAllEqual(4, q.size())

    q2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.int32, shapes=tensor_shape.TensorShape([3]))
    q2.enqueue(([1, 2, 3],))
    q2.enqueue_many(([[1, 2, 3]],))
