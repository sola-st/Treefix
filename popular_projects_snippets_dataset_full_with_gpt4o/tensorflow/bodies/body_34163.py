# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PriorityQueue(2000, (dtypes.string, dtypes.string), (
        (), ()))
    elem = np.random.randint(-100, 100, size=1000).astype(np.int64)
    side_value_0 = np.random.rand(1000).astype(bytes)
    side_value_1 = np.random.rand(1000).astype(bytes)
    q.enqueue_many((elem, side_value_0, side_value_1)).run()
    deq = q.dequeue_many(1000)
    deq_elem, deq_value_0, deq_value_1 = self.evaluate(deq)

    allowed = {}
    for e, v0, v1 in zip(elem, side_value_0, side_value_1):
        if e not in allowed:
            allowed[e] = set()
        allowed[e].add((v0, v1))

    self.assertAllEqual(deq_elem, sorted(elem))
    for e, dv0, dv1 in zip(deq_elem, deq_value_0, deq_value_1):
        self.assertTrue((dv0, dv1) in allowed[e])
