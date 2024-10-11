# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.int32, (4, 4, 4, 4))
elems = np.array([[[[[x] * 4] * 4] * 4] * 4 for x in range(10)], np.int32)

self.evaluate(q.enqueue_many((elems,)))
self.assertAllEqual(self.evaluate(q.dequeue_many(10)), elems)
