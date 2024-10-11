# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shapes=())

self.assertEqual([], self.evaluate(q.dequeue_many(0)).tolist())
self.evaluate(q.enqueue((10.0,)))
self.assertEqual([], self.evaluate(q.dequeue_many(0)).tolist())
