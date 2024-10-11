# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, ((),))
    elems = [10.0, 20.0, 30.0, 40.0]
    enqueue_op = q.enqueue_many((elems,))
    dequeued_t = q.dequeue()
    enqueue_op.run()
    enqueue_op.run()

    for i in range(8):
        vals = self.evaluate(dequeued_t)
        self.assertEqual([elems[i % 4]], vals)
