# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
self.assertAllEqual(elems[0:3], self.evaluate(dequeued_t))
with self.assertRaises(errors_impl.OutOfRangeError):
    self.evaluate(dequeued_t)
self.assertEqual(elems[3], self.evaluate(cleanup_dequeue_t))
