# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
self.assertEqual([], q.size().get_shape())

self.evaluate(q.enqueue((10.0,)))
self.assertEqual(1, self.evaluate(q.size()))
self.evaluate(q.dequeue())
self.assertEqual(0, self.evaluate(q.size()))
