# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
# Expect the operation to fail due to the shape not being constrained.
with self.assertRaisesOpError("specified shapes"):
    self.evaluate(q.dequeue_many(0))
