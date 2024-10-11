# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    # Run one producer thread for each element in elems.
    def enqueue(enqueue_op):
        self.evaluate(enqueue_op)

    threads = [
        self.checkedThread(
            target=enqueue, args=(e,)) for e in enqueue_ops
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Dequeue every element using a single thread.
    results = []
    for _ in range(len(elems)):
        results.append(dequeued_t.eval())
    self.assertItemsEqual(elems, results)
