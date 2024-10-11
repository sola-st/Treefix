# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, (
        (None, None),))
    empty_t = constant_op.constant(
        [], dtype=dtypes_lib.float32, shape=[0, 2, 3])
    enqueue_op = q.enqueue_many((empty_t,))
    size_t = q.size()

    self.assertEqual([0], self.evaluate(size_t))
    enqueue_op.run()
    self.assertEqual([0], self.evaluate(size_t))
