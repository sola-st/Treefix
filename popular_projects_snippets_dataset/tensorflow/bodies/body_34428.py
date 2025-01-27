# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(5, dtypes_lib.int32, ((),))
    elem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    enq = q.enqueue_many((elem,))
    deq = q.dequeue()
    size_op = q.size()

    enq_done = []

    def blocking_enqueue():
        enq_done.append(False)
        # This will fill the queue and then block until enough dequeues happen.
        self.evaluate(enq)
        enq_done.append(True)

    thread = self.checkedThread(target=blocking_enqueue)
    thread.start()

    # The enqueue should start and then block.
    results = []
    results.append(
        self.evaluate(deq))  # Will only complete after the enqueue starts.
    self.assertEqual(len(enq_done), 1)
    self.assertEqual(self.evaluate(size_op), 5)

    for _ in range(3):
        results.append(self.evaluate(deq))

    time.sleep(0.1)
    self.assertEqual(len(enq_done), 1)
    self.assertEqual(self.evaluate(size_op), 5)

    # This dequeue will unblock the thread.
    results.append(self.evaluate(deq))
    time.sleep(0.1)
    self.assertEqual(len(enq_done), 2)
    thread.join()

    for i in range(5):
        self.assertEqual(self.evaluate(size_op), 5 - i)
        results.append(self.evaluate(deq))
        self.assertEqual(self.evaluate(size_op), 5 - i - 1)

    self.assertAllEqual(elem, results)
