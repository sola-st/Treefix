# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(4, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0]
    enqueue_op = q.enqueue_many((elems,))
    blocking_enqueue_op = q.enqueue_many(([50.0, 60.0],))
    close_op = q.close()
    size_t = q.size()

    enqueue_op.run()
    self.assertEqual(size_t.eval(), 3)

    def blocking_enqueue():
        # This will block until the dequeue after the close.
        self.evaluate(blocking_enqueue_op)

    thread1 = self.checkedThread(target=blocking_enqueue)
    thread1.start()

    # First blocking_enqueue_op of blocking_enqueue has enqueued 1 of 2
    # elements, and is blocked waiting for one more element to be dequeue.
    for i in range(50):
        queue_size = self.evaluate(size_t)
        if queue_size == 4:
            break
        elif i == 49:
            self.fail(
                "Blocking enqueue op did not execute within the expected time.")

        time.sleep(0.1)

    def blocking_close():
        self.evaluate(close_op)

    thread2 = self.checkedThread(target=blocking_close)
    thread2.start()

    # Unblock the first blocking_enqueue_op in blocking_enqueue.
    q.dequeue().eval()

    thread2.join()
    thread1.join()

    # At this point the close operation will complete, so the next enqueue
    # will fail.
    with self.assertRaisesRegex(errors_impl.CancelledError, "closed"):
        self.evaluate(blocking_enqueue_op)
