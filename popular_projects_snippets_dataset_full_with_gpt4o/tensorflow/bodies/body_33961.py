# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(
        10, [dtypes_lib.int32, dtypes_lib.int32], shapes=[(), (2,)])
    q.enqueue_many([[1, 2, 3, 4], [[1, 1], [2, 2], [3, 3], [4, 4]]]).run()
    self.assertEqual(4, q.size().eval())
