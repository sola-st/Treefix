# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(
        10, 0, (dtypes_lib.float32, dtypes_lib.int32))
    float_elems = [10.0, 20.0, 30.0, 40.0]
    int_elems = [[1, 2], [3, 4], [5, 6], [7, 8]]
    enqueue_op = q.enqueue_many((float_elems, int_elems))
    dequeued_t = q.dequeue()

    enqueue_op.run()
    enqueue_op.run()

    results = []
    for _ in range(8):
        float_val, int_val = self.evaluate(dequeued_t)
        results.append((float_val, [int_val[0], int_val[1]]))
    expected = list(zip(float_elems, int_elems)) * 2
    self.assertItemsEqual(expected, results)
