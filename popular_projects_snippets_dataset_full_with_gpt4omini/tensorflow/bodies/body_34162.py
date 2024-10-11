# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PriorityQueue(2000, (dtypes.string, dtypes.string), (
        (), ()))
    elem = np.random.randint(-5, 5, size=100).astype(np.int64)
    side_value_0 = np.random.rand(100).astype(bytes)
    side_value_1 = np.random.rand(100).astype(bytes)

    batch = 5
    enqueue_ops = [
        q.enqueue_many((elem[i * batch:(i + 1) * batch],
                        side_value_0[i * batch:(i + 1) * batch],
                        side_value_1[i * batch:(i + 1) * batch]))
        for i in range(20)
    ]

    # Run one producer thread for each element in elems.
    def enqueue(enqueue_op):
        self.evaluate(enqueue_op)

    dequeue_op = q.dequeue_many(100)

    enqueue_threads = [
        self.checkedThread(
            target=enqueue, args=(op,)) for op in enqueue_ops
    ]

    for t in enqueue_threads:
        t.start()

    deq_elem, deq_value_0, deq_value_1 = self.evaluate(dequeue_op)

    for t in enqueue_threads:
        t.join()

    allowed = {}
    missed = set()
    for e, v0, v1 in zip(elem, side_value_0, side_value_1):
        if e not in allowed:
            allowed[e] = set()
        allowed[e].add((v0, v1))
        missed.add((v0, v1))

    self.assertAllEqual(deq_elem, sorted(elem))
    for e, dv0, dv1 in zip(deq_elem, deq_value_0, deq_value_1):
        self.assertTrue((dv0, dv1) in allowed[e])
        missed.remove((dv0, dv1))
    self.assertEqual(missed, set())
