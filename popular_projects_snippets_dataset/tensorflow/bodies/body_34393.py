# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, ())
elems = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

self.evaluate(q.enqueue_many((elems,)))

self.assertAllEqual(elems[0:4], self.evaluate(q.dequeue_many(4)))
self.assertAllEqual(elems[4:8], self.evaluate(q.dequeue_many(4)))
