# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
results.append(self.evaluate(dequeued_t))
results.append(self.evaluate(dequeued_t))

self.assertItemsEqual(elems, results)
# Expect the operation to fail due to the queue being closed.
with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                            "is closed and has insufficient"):
    self.evaluate(dequeued_t)
