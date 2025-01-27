# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q1 = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    q2 = data_flow_ops.RandomShuffleQueue(15, 0, dtypes_lib.float32)
    enq_q = data_flow_ops.RandomShuffleQueue.from_list(3, [q1, q2])
    with self.assertRaisesOpError("is not in"):
        enq_q.dequeue().eval()
