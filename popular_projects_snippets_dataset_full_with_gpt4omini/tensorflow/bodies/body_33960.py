# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(
        10, dtypes_lib.float32, shapes=((3, 2),))
    enqueue_correct_op = q.enqueue(([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],))
    enqueue_correct_op.run()
    with self.assertRaises(ValueError):
        q.enqueue(([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],))
    self.assertEqual(1, q.size().eval())
