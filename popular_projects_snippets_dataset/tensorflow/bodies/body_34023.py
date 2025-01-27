# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_many(4)

    enqueue_op.run()

    def dequeue():
        self.assertAllEqual(elems, self.evaluate(dequeued_t))
        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                    "is closed and has insufficient"):
            self.evaluate(dequeued_t)

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    close_op.run()
    dequeue_thread.join()
