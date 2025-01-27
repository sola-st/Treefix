# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10,
                                       (dtypes_lib.int32, dtypes_lib.float32),
                                       ((), ()))
    elems = [(5, 10.0), (10, 20.0), (15, 30.0)]
    enqueue_ops = [q.enqueue((x, y)) for x, y in elems]
    dequeued_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    for i in range(len(elems)):
        x_val, y_val = self.evaluate(dequeued_t)
        x, y = elems[i]
        self.assertEqual([x], x_val)
        self.assertEqual([y], y_val)
