# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shapes=(3, 2))
self.evaluate(q.enqueue(([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],)))
with self.assertRaises(ValueError):
    q.enqueue(([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],))
self.assertEqual(1, self.evaluate(q.size()))
