# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
if self.q2 is None:
    self.q2 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
self.q2.enqueue(x)
self.q2.enqueue(x + 3)
self.q1.enqueue(self.q2.dequeue())
