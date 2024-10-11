# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    min_size = 2
    q = data_flow_ops.RandomShuffleQueue(10, min_size, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue()

    enqueue_op.run()

    results = []

    # Manually dequeue until we hit min_size.
    results.append(self.evaluate(dequeued_t))
    results.append(self.evaluate(dequeued_t))

    def blocking_dequeue():
        results.append(self.evaluate(dequeued_t))
        results.append(self.evaluate(dequeued_t))

        self.assertItemsEqual(elems, results)
        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                    "is closed and has insufficient"):
            self.evaluate(dequeued_t)

    dequeue_thread = self.checkedThread(target=blocking_dequeue)
    dequeue_thread.start()
    time.sleep(0.1)

    # The dequeue thread blocked when it hit the min_size requirement.
    self.assertEqual(len(results), 2)
    close_op.run()
    dequeue_thread.join()
    # Once the queue is closed, the min_size requirement is lifted.
    self.assertEqual(len(results), 4)
