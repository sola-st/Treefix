# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.float32), (
    (), ()))

@def_function.function
def _f():
    enq = q.enqueue_many(([], []))
    self.assertEqual(dtypes_lib.int32, enq.inputs[1].dtype)
    self.assertEqual(dtypes_lib.float32, enq.inputs[2].dtype)

_f()
