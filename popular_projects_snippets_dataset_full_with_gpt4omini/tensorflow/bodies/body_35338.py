# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    dequeued_t = q.dequeue()
    size = q.size()
    self.assertEqual([], size.get_shape())

    enqueue_op.run()
    self.assertEqual([1], self.evaluate(size))
    dequeued_t.op.run()
    self.assertEqual([0], self.evaluate(size))
