# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(4, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    blocking_enqueue_op = q.enqueue((50.0,))
    dequeued_t = q.dequeue()
    close_op = q.close()

    enqueue_op.run()

    def blocking_enqueue():
        # Expect the operation to succeed since it will complete
        # before the queue is closed.
        self.evaluate(blocking_enqueue_op)

        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.CancelledError, "closed"):
            self.evaluate(blocking_enqueue_op)

    thread1 = self.checkedThread(target=blocking_enqueue)
    thread1.start()

    # The close_op should run after the first blocking_enqueue_op has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    def blocking_close():
        self.evaluate(close_op)

    thread2 = self.checkedThread(target=blocking_close)
    thread2.start()

    # Wait for the close op to block before unblocking the enqueue.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    results = []
    # Dequeue to unblock the first blocking_enqueue_op, after which the
    # close will complete.
    results.append(dequeued_t.eval())
    self.assertTrue(results[0] in elems)
    thread2.join()
    thread1.join()
