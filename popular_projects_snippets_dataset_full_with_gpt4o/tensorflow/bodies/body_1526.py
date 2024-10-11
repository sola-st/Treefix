# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    enqueue_op = q.enqueue((10.0,))
    dequeued_t = q.dequeue()
    size = q.size()
    self.assertEqual([], size.get_shape())

    enqueue_op.run()
    self.assertEqual(1, self.evaluate(size))
    dequeued_t.op.run()
    self.assertEqual(0, self.evaluate(size))
