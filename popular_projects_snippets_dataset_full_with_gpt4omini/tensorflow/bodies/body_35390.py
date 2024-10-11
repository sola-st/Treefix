# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# Expect the operation to succeed since it will complete
# before the queue is closed.
self.evaluate(blocking_enqueue_op)

# Expect the operation to fail due to the queue being closed.
with self.assertRaisesRegex(errors_impl.CancelledError, "closed"):
    self.evaluate(blocking_enqueue_op)
