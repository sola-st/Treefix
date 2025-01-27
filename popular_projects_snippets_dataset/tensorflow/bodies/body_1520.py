# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32)
    elems = [10.0, 20.0, 30.0]
    enqueue_ops = [q.enqueue((x,)) for x in elems]
    dequeued_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    for i in range(len(elems)):
        vals = self.evaluate(dequeued_t)
        self.assertEqual([elems[i]], vals)
