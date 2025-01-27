# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(1000, dtypes_lib.float32, shapes=((),))
    elems = [10.0 * x for x in range(1000)]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_many(100)

    enqueue_op.run()

    # Dequeue 100 items in parallel on 10 threads.
    dequeued_elems = []

    def dequeue():
        dequeued_elems.extend(self.evaluate(dequeued_t))

    threads = [self.checkedThread(target=dequeue) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    self.assertItemsEqual(elems, dequeued_elems)
