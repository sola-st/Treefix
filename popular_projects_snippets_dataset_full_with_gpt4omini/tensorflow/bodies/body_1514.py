# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
    self.evaluate(q.enqueue(1))
    q2 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
    self.evaluate(q2.enqueue(2))
    self.assertAllEqual(self.evaluate(q2.dequeue()), 2)
    self.assertAllEqual(self.evaluate(q.dequeue()), 1)
