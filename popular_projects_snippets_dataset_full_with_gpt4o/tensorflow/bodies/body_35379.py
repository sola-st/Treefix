# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_many(3)
    cleanup_dequeue_t = q.dequeue_many(q.size())

    enqueue_op.run()

    results = []

    def dequeue():
        results.extend(self.evaluate(dequeued_t))
        self.assertEqual(len(results), 3)
        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                    "is closed and has insufficient"):
            self.evaluate(dequeued_t)
        # While the last dequeue failed, we want to insure that it returns
        # any elements that it potentially reserved to dequeue. Thus the
        # next cleanup should return a single element.
        results.extend(self.evaluate(cleanup_dequeue_t))

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    close_op.run()
    dequeue_thread.join()
    self.assertEqual(len(results), 4)
