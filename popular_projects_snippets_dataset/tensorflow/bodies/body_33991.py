# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
q = data_flow_ops.PaddingFIFOQueue(10,
                                   (dtypes_lib.int32, dtypes_lib.float32), (
                                       (), ()))
enq = q.enqueue_many(([], []))
self.assertEqual(dtypes_lib.int32, enq.inputs[1].dtype)
self.assertEqual(dtypes_lib.float32, enq.inputs[2].dtype)
