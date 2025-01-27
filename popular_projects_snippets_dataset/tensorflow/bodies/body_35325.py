# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shapes=tensor_shape.TensorShape([3, 2]))
    enqueue_correct_op = q.enqueue(([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],))
    enqueue_correct_op.run()
    self.assertAllEqual(1, q.size())
    with self.assertRaises(ValueError):
        q.enqueue(([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],))
