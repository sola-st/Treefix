# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
self.q1 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
self.q2 = None
