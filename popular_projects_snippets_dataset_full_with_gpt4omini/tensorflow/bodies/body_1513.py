# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
    self.evaluate(q.enqueue([1]))
    self.evaluate(q.enqueue([2]))
    self.evaluate(q.enqueue([3]))
    a, b, c = self.evaluate([q.dequeue(), q.dequeue(), q.dequeue()])
    self.assertAllEqual(set([1, 2, 3]), set([a, b, c]))
