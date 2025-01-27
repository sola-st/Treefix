# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
with self.cached_session():
    q = data_flow_ops.PriorityQueue(2000, (dtypes.int64), (()))
    elem = np.random.randint(-100, 100, size=1000).astype(np.int64)
    q.enqueue_many((elem, elem)).run()
    dequeue_op = q.dequeue()
    deq_values = np.hstack(dequeue_op[0].eval() for _ in range(1000))
    self.assertAllEqual(deq_values, sorted(elem))
