# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.int32,
                                 dtypes_lib.int32), ((), (), ()))

with self.assertRaises(ValueError):
    q.enqueue_many(([1, 2, 3], [1, 2], [1, 2, 3]))

with self.assertRaises(ValueError):
    q.enqueue_many(
        ([1, 2, 3], [1, 2], array_ops.placeholder(dtypes_lib.int32)))

with self.assertRaises(ValueError):
    q.enqueue_many(
        (array_ops.placeholder(dtypes_lib.int32), [1, 2], [1, 2, 3]))
