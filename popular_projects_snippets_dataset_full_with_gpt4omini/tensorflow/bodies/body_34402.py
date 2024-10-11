# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.float32), (
    (), ()))

@def_function.function
def _f():
    with self.assertRaises(ValueError):
        q.enqueue((array_ops.placeholder(dtypes_lib.int32),
                   array_ops.placeholder(dtypes_lib.int32)))

    with self.assertRaises(ValueError):
        q.enqueue_many((array_ops.placeholder(dtypes_lib.int32),
                        array_ops.placeholder(dtypes_lib.int32)))

_f()
