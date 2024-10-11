# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.assertRaises(ValueError):
    q.enqueue((array_ops.placeholder(dtypes_lib.int32),
               array_ops.placeholder(dtypes_lib.int32)))

with self.assertRaises(ValueError):
    q.enqueue_many((array_ops.placeholder(dtypes_lib.int32),
                    array_ops.placeholder(dtypes_lib.int32)))
