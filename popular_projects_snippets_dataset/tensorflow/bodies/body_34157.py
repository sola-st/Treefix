# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PriorityQueue(10, (dtypes.int64), (()))

    num_threads = 40
    enqueue_counts = np.random.randint(10, size=num_threads)
    enqueue_values = [
        np.random.randint(
            5, size=count) for count in enqueue_counts
    ]
    enqueue_ops = [
        q.enqueue_many((values, values)) for values in enqueue_values
    ]
    shuffled_counts = copy.deepcopy(enqueue_counts)
    random.shuffle(shuffled_counts)
    dequeue_ops = [q.dequeue_many(count) for count in shuffled_counts]
    all_enqueued_values = np.hstack(enqueue_values)

    # Run one producer thread for each element in elems.
    def enqueue(enqueue_op):
        self.evaluate(enqueue_op)

    dequeued = []

    def dequeue(dequeue_op):
        (dequeue_indices, dequeue_values) = self.evaluate(dequeue_op)
        self.assertAllEqual(dequeue_indices, dequeue_values)
        dequeued.extend(dequeue_indices)

    enqueue_threads = [
        self.checkedThread(
            target=enqueue, args=(op,)) for op in enqueue_ops
    ]
    dequeue_threads = [
        self.checkedThread(
            target=dequeue, args=(op,)) for op in dequeue_ops
    ]

    # Dequeue and check
    for t in dequeue_threads:
        t.start()
    for t in enqueue_threads:
        t.start()
    for t in enqueue_threads:
        t.join()
    for t in dequeue_threads:
        t.join()

    self.assertAllEqual(sorted(dequeued), sorted(all_enqueued_values))
