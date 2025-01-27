# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(3, 0, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    def enqueue():
        # The enqueue_ops should run after the dequeue op has blocked.
        # TODO(mrry): Figure out how to do this without sleeping.
        time.sleep(0.1)
        for enqueue_op in enqueue_ops:
            self.evaluate(enqueue_op)

    results = []

    def dequeue():
        for _ in range(len(elems)):
            results.append(self.evaluate(dequeued_t))

    enqueue_thread = self.checkedThread(target=enqueue)
    dequeue_thread = self.checkedThread(target=dequeue)
    enqueue_thread.start()
    dequeue_thread.start()
    enqueue_thread.join()
    dequeue_thread.join()

    self.assertItemsEqual(elems, results)
