# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(4, 0, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    blocking_enqueue_op = q.enqueue_many(([50.0, 60.0],))
    dequeued_t = q.dequeue()

    enqueue_op.run()

    def blocking_enqueue():
        self.evaluate(blocking_enqueue_op)

    thread = self.checkedThread(target=blocking_enqueue)
    thread.start()
    # The dequeue ops should run after the blocking_enqueue_op has blocked.
    # TODO(mrry): Figure out how to do this without sleeping.
    time.sleep(0.1)

    results = []
    for _ in elems:
        time.sleep(0.01)
        results.append(dequeued_t.eval())
    results.append(dequeued_t.eval())
    results.append(dequeued_t.eval())
    self.assertItemsEqual(elems + [50.0, 60.0], results)
    # There wasn't room for 50.0 or 60.0 in the queue when the first
    # element was dequeued.
    self.assertNotEqual(50.0, results[0])
    self.assertNotEqual(60.0, results[0])
    # Similarly for 60.0 and the second element.
    self.assertNotEqual(60.0, results[1])
    thread.join()
