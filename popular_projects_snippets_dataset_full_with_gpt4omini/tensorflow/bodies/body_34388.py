# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
empty_t = constant_op.constant(
    [], dtype=dtypes_lib.float32, shape=[0, 2, 3])

self.assertEqual([0], self.evaluate(q.size()))
self.evaluate(q.enqueue_many((empty_t,)))
self.assertEqual([0], self.evaluate(q.size()))
