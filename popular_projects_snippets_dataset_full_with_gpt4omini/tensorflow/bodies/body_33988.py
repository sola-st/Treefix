# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.int32, (
        (4, None, 4, None),))
    elems = np.array([[[[[x] * 4] * 4] * 4] * 4 for x in range(10)], np.int32)
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue_many(10)

    enqueue_op.run()
    self.assertAllEqual(dequeued_t, elems)
