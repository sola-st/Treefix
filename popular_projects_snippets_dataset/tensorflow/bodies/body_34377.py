# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
self.evaluate(q.enqueue(1))
q2 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
self.evaluate(q2.enqueue(2))
self.assertAllEqual(self.evaluate(q2.dequeue()), 2)
self.assertAllEqual(self.evaluate(q.dequeue()), 1)
