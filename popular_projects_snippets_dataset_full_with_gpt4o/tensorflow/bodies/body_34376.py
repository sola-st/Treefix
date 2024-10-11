# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
self.evaluate(q.enqueue_many([[1, 2, 3]]))
a, b, c = self.evaluate([q.dequeue(), q.dequeue(), q.dequeue()])
self.assertAllEqual(set([1, 2, 3]), set([a, b, c]))
