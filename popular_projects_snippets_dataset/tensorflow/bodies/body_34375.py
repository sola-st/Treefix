# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(
    10, [dtypes_lib.int32, dtypes_lib.int32], shapes=[(), (2,)])
self.evaluate(
    q.enqueue_many([[1, 2, 3, 4], [[1, 1], [2, 2], [3, 3], [4, 4]]]))
self.assertEqual(4, self.evaluate(q.size()))
