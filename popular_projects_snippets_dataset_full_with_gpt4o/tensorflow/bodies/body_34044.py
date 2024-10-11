# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(4, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    blocking_enqueue_op = q.enqueue((50.0,))
    close_op = q.close()
    dequeued_t = q.dequeue()

    enqueue_op.run()

    def blocking_enqueue():
        # Expect the operation to succeed once the dequeue op runs.
        self.evaluate(blocking_enqueue_op)

    enqueue_thread = self.checkedThread(target=blocking_enqueue)
    enqueue_thread.start()

    # The close_op should run after the blocking_enqueue_op has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    def close():
        self.evaluate(close_op)

    close_thread = self.checkedThread(target=close)
    close_thread.start()

    # The dequeue will unblock both threads.
    self.assertEqual(10.0, self.evaluate(dequeued_t))
    enqueue_thread.join()
    close_thread.join()

    for elem in [20.0, 30.0, 40.0, 50.0]:
        self.assertEqual(elem, self.evaluate(dequeued_t))
    self.assertEqual(0, q.size().eval())
