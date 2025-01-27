# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 5, dtypes_lib.float32)
    empty_t = constant_op.constant(
        [], dtype=dtypes_lib.float32, shape=[0, 2, 3])
    enqueue_op = q.enqueue_many((empty_t,))
    size_t = q.size()

    self.assertEqual(0, self.evaluate(size_t))
    enqueue_op.run()
    self.assertEqual(0, self.evaluate(size_t))
