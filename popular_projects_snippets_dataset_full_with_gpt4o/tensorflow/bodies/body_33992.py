# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
q = data_flow_ops.PaddingFIFOQueue(10,
                                   (dtypes_lib.int32, dtypes_lib.float32), (
                                       (), ()))

with self.assertRaises(ValueError):
    q.enqueue((array_ops.placeholder(dtypes_lib.int32),
               array_ops.placeholder(dtypes_lib.int32)))

with self.assertRaises(ValueError):
    q.enqueue_many((array_ops.placeholder(dtypes_lib.int32),
                    array_ops.placeholder(dtypes_lib.int32)))
