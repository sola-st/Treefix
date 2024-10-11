# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
self.assertAllEqual(elems[:3], self.evaluate(dequeued_t))
self.assertAllEqual(elems[3:], self.evaluate(dequeued_t))
