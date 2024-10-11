# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    num_queues = 10
    qlist = []
    for _ in range(num_queues):
        qlist.append(
            data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32))
    # Enqueue/Dequeue into a dynamically selected queue
    for _ in range(20):
        index = np.random.randint(num_queues)
        q = data_flow_ops.RandomShuffleQueue.from_list(index, qlist)
        q.enqueue((10.,)).run()
        self.assertEqual(q.dequeue().eval(), 10.0)
