# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 5, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    self.assertAllEqual(0, q.size())
    enqueue_op.run()
    self.assertAllEqual(1, q.size())
