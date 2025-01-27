# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    # Run one producer thread for each element in elems.
    def enqueue(enqueue_op):
        self.evaluate(enqueue_op)

    threads = [
        self.checkedThread(
            target=enqueue, args=(e,)) for e in enqueue_ops
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Dequeue every element using a single thread.
    results = []
    for _ in range(len(elems)):
        results.append(self.evaluate(dequeued_t))
    self.assertItemsEqual(elems, results)
