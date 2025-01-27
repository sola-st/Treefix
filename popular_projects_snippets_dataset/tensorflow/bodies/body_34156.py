# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
(dequeue_indices, dequeue_values) = self.evaluate(dequeue_op)
self.assertAllEqual(dequeue_indices, dequeue_values)
dequeued.extend(dequeue_indices)
