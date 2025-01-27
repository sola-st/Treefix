# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
self.assertAllEqual(elems[0:3], sess.run(dequeued_t))
with self.assertRaises(errors_impl.OutOfRangeError):
    sess.run(dequeued_t)
self.assertEqual(elems[3], sess.run(cleanup_dequeue_t))
