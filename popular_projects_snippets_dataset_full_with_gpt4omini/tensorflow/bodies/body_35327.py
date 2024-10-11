# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(
        10, 0, [dtypes_lib.int32, dtypes_lib.int32], shapes=[(), (1,)])
    q.enqueue_many([[1, 2, 3, 4], [[5], [6], [7], [8]]]).run()
    q.enqueue([9, [10]]).run()
    dequeue_t = q.dequeue()
    results = []
    for _ in range(2):
        a, b = self.evaluate(dequeue_t)
        results.append((a, b))
    a, b = self.evaluate(q.dequeue_many(3))
    for i in range(3):
        results.append((a[i], b[i]))
    self.assertItemsEqual([(1, [5]), (2, [6]), (3, [7]), (4, [8]), (9, [10])],
                          results)
