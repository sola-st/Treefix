# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(
        10, 0, (dtypes_lib.int32, dtypes_lib.float32))
    elems = [(5, 10.0), (10, 20.0), (15, 30.0)]
    enqueue_ops = [q.enqueue((x, y)) for x, y in elems]
    dequeued_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    results = []
    for _ in range(len(elems)):
        x, y = self.evaluate(dequeued_t)
        results.append((x, y))
    self.assertItemsEqual(elems, results)
