# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(50, dtypes_lib.float32, shapes=())
    initial_elements = [10.0] * 49
    q.enqueue_many((initial_elements,)).run()

    enqueue_op = q.enqueue((20.0,))
    dequeued_t = q.dequeue()

    def enqueue():
        for _ in range(100):
            self.evaluate(enqueue_op)

    def dequeue():
        for _ in range(100):
            self.assertTrue(self.evaluate(dequeued_t) in (10.0, 20.0))

    enqueue_threads = [self.checkedThread(target=enqueue) for _ in range(10)]
    dequeue_threads = [self.checkedThread(target=dequeue) for _ in range(10)]
    for enqueue_thread in enqueue_threads:
        enqueue_thread.start()
    for dequeue_thread in dequeue_threads:
        dequeue_thread.start()
    for enqueue_thread in enqueue_threads:
        enqueue_thread.join()
    for dequeue_thread in dequeue_threads:
        dequeue_thread.join()

    # Dequeue the initial count of elements to clean up.
    cleanup_elems = q.dequeue_many(49).eval()
    for elem in cleanup_elems:
        self.assertTrue(elem in (10.0, 20.0))
