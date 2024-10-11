# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session() as sess, self.test_scope():
    q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.float32))
    elems = [(5, 10.0), (10, 20.0), (15, 30.0)]
    enqueue_ops = [q.enqueue((x, y)) for x, y in elems]
    dequeued_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()

    for i in range(len(elems)):
        x_val, y_val = sess.run(dequeued_t)
        x, y = elems[i]
        self.assertEqual([x], x_val)
        self.assertEqual([y], y_val)
