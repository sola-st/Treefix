# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q = data_flow_ops.RandomShuffleQueue(10, 0, dtypes_lib.int32, (
        (4, 4, 4, 4)))
    elems = np.array([[[[[x] * 4] * 4] * 4] * 4 for x in range(10)], np.int32)
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_many(10)

    enqueue_op.run()
    self.assertItemsEqual(dequeued_t.eval().tolist(), elems.tolist())
