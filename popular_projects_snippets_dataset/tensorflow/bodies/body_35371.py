# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    close_op = q.close()
    dequeued_t = q.dequeue()

    finished = []  # Needs to be a mutable type

    def dequeue():
        # Expect the operation to fail due to the queue being closed.
        with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                                    "is closed and has insufficient"):
            self.evaluate(dequeued_t)
        finished.append(True)

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    self.assertEqual(len(finished), 0)
    close_op.run()
    dequeue_thread.join()
    self.assertEqual(len(finished), 1)
