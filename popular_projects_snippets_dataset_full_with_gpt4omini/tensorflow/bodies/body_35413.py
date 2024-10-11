# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(2, 0, dtypes_lib.int32, ((),))
    elem = np.arange(4, dtype=np.int32)
    enq_list = [q.enqueue((e,)) for e in elem]
    deq = q.dequeue_many(4)

    results = []

    def blocking_dequeue():
        # Will only complete after 4 enqueues complete.
        results.extend(self.evaluate(deq))

    thread = self.checkedThread(target=blocking_dequeue)
    thread.start()
    # The dequeue should start and then block.
    for enq in enq_list:
        # TODO(mrry): Figure out how to do this without sleeping.
        time.sleep(0.1)
        self.assertEqual(len(results), 0)
        self.evaluate(enq)

    # Enough enqueued to unblock the dequeue
    thread.join()
    self.assertItemsEqual(elem, results)
