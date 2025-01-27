# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
self.assertAllEqual(elems, self.evaluate(dequeued_t))
# Expect the operation to fail due to the queue being closed.
with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                            "is closed and has insufficient"):
    self.evaluate(dequeued_t)
