# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
elems = [10.0, 20.0, 30.0, 40.0]
self.evaluate(q.enqueue_many((elems,)))
self.evaluate(q.enqueue_many((elems,)))

for i in range(8):
    vals = self.evaluate(q.dequeue())
    self.assertEqual([elems[i % 4]], vals)
