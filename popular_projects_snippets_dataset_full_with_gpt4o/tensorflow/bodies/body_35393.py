# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# This will block until the dequeue after the close.
self.evaluate(blocking_enqueue_op)
