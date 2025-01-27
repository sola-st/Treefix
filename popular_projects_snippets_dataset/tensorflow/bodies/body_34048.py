# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(1, dtypes_lib.float32, ((),))
    enqueue_op = q.enqueue((10.0,))
    size_t = q.size()

    enqueue_op.run()
    for _ in range(500):
        self.assertEqual(self.evaluate(size_t), [1])
