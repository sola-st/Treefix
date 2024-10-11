# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PriorityQueue(2000, (dtypes.int64), (()))

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

    dequeue_wait = threading.Condition()

    # Run one producer thread for each element in elems.
    def enqueue(enqueue_op):
        self.evaluate(enqueue_op)

    def dequeue(dequeue_op, dequeued):
        (dequeue_indices, dequeue_values) = self.evaluate(dequeue_op)
        self.assertAllEqual(dequeue_indices, dequeue_values)
        dequeue_wait.acquire()
        dequeued.extend(dequeue_indices)
        dequeue_wait.release()

    dequeued = []
    enqueue_threads = [
        self.checkedThread(
            target=enqueue, args=(op,)) for op in enqueue_ops
    ]
    dequeue_threads = [
        self.checkedThread(
            target=dequeue, args=(op, dequeued)) for op in dequeue_ops
    ]

    for t in enqueue_threads:
        t.start()
    for t in enqueue_threads:
        t.join()
    # Dequeue and check
    for t in dequeue_threads:
        t.start()
    for t in dequeue_threads:
        t.join()

    # We can't guarantee full sorting because we can't guarantee
    # that the dequeued.extend() call runs immediately after the
    # self.evaluate() call.  Here we're just happy everything came out.
    self.assertAllEqual(set(dequeued), set(all_enqueued_values))
