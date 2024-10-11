# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(
        capacity=10,
        min_after_dequeue=2,
        dtypes=dtypes_lib.float32,
        shapes=((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    close_op = q.close()
    dequeued_t = q.dequeue_up_to(3)

    enqueue_op.run()

    results = []

    def dequeue():
        results.extend(self.evaluate(dequeued_t))
        self.assertEqual(3, len(results))
        # min_after_dequeue is 2, we ask for 3 elements, and we end up only
        # getting the remaining 1.
        results.extend(self.evaluate(dequeued_t))
        self.assertEqual(4, len(results))

    dequeue_thread = self.checkedThread(target=dequeue)
    dequeue_thread.start()
    # The close_op should run after the dequeue_thread has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)
    close_op.run()
    dequeue_thread.join()
    self.assertItemsEqual(results, elems)
