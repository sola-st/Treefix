# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(1000, dtypes_lib.float32, shapes=())
    elems = [10.0 * x for x in range(100)]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_many(1000)

    # Enqueue 100 items in parallel on 10 threads.
    def enqueue():
        self.evaluate(enqueue_op)

    threads = [self.checkedThread(target=enqueue) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    self.assertCountEqual(self.evaluate(dequeued_t), elems * 10)
