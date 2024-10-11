# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_many(4)

    enqueue_op.run()

    progress = []  # Must be mutable

    def dequeue():
        self.assertItemsEqual(elems, self.evaluate(dequeued_t))
        progress.append(1)
        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                    "is closed and has insufficient"):
            self.evaluate(dequeued_t)
        progress.append(2)

    self.assertEqual(len(progress), 0)
    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    for _ in range(100):
        time.sleep(0.01)
        if len(progress) == 1:
            break
    self.assertEqual(len(progress), 1)
    time.sleep(0.01)
    close_op.run()
    dequeue_thread.join()
    self.assertEqual(len(progress), 2)
