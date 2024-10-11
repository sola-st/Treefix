# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(4, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_many(3)
    cleanup_dequeue_t = q.dequeue()

    def enqueue():
        self.evaluate(enqueue_op)

    def dequeue():
        self.assertAllEqual(elems[0:3], self.evaluate(dequeued_t))
        with self.assertRaises(errors_impl.OutOfRangeError):
            self.evaluate(dequeued_t)
        self.assertEqual(elems[3], self.evaluate(cleanup_dequeue_t))

    def close():
        self.evaluate(close_op)

    enqueue_thread = self.checkedThread(target=enqueue)
    enqueue_thread.start()

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    close_thread = self.checkedThread(target=close)
    close_thread.start()

    enqueue_thread.join()
    dequeue_thread.join()
    close_thread.join()
