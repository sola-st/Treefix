# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(4, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    blocking_enqueue_op = q.enqueue_many(([50.0, 60.0],))
    dequeued_t = q.dequeue()

    enqueue_op.run()

    def blocking_enqueue():
        self.evaluate(blocking_enqueue_op)

    thread = self.checkedThread(target=blocking_enqueue)
    thread.start()
    # The dequeue ops should run after the blocking_enqueue_op has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    for elem in elems:
        self.assertEqual([elem], self.evaluate(dequeued_t))
        time.sleep(0.01)
    self.assertEqual([50.0], self.evaluate(dequeued_t))
    self.assertEqual([60.0], self.evaluate(dequeued_t))

    # Make sure the thread finishes before exiting.
    thread.join()
