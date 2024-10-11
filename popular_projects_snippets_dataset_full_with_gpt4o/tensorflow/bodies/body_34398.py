# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.int32), ((),
                                                                       (2)))

with self.assertRaises(ValueError):
    q.enqueue(([1, 2], [2, 2]))

with self.assertRaises(ValueError):
    q.enqueue_many((7, [[1, 2], [3, 4], [5, 6]]))
