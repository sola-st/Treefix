# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.RandomShuffleQueue(
        10, 0, (dtypes_lib.float32, dtypes_lib.int32), shapes=((), (2,)))
    float_elems = [
        10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0
    ]
    int_elems = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
                 [15, 16], [17, 18], [19, 20]]
    enqueue_op = q.enqueue_many((float_elems, int_elems))
    dequeued_t = q.dequeue_many(4)
    dequeued_single_t = q.dequeue()

    enqueue_op.run()

    results = []
    float_val, int_val = self.evaluate(dequeued_t)
    self.assertEqual(float_val.shape, dequeued_t[0].get_shape())
    self.assertEqual(int_val.shape, dequeued_t[1].get_shape())
    results.extend(zip(float_val, int_val.tolist()))

    float_val, int_val = self.evaluate(dequeued_t)
    results.extend(zip(float_val, int_val.tolist()))

    float_val, int_val = self.evaluate(dequeued_single_t)
    self.assertEqual(float_val.shape, dequeued_single_t[0].get_shape())
    self.assertEqual(int_val.shape, dequeued_single_t[1].get_shape())
    results.append((float_val, int_val.tolist()))

    float_val, int_val = self.evaluate(dequeued_single_t)
    results.append((float_val, int_val.tolist()))

    self.assertItemsEqual(zip(float_elems, int_elems), results)
