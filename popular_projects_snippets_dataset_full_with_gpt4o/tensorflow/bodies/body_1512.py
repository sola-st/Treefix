# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
with self.session(), self.test_scope():
    q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shapes=(3, 2))
    enqueue_correct_op = q.enqueue(([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],))
    enqueue_correct_op.run()
    with self.assertRaises(ValueError):
        q.enqueue(([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],))
    self.assertEqual(1, self.evaluate(q.size()))
