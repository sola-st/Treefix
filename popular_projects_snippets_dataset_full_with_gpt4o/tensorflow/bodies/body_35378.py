# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
results.extend(self.evaluate(dequeued_t))
self.assertEqual(len(results), 3)
# Expect the operation to fail due to the queue being closed.
with self.assertRaisesRegex(errors_impl.OutOfRangeError,
                            "is closed and has insufficient"):
    self.evaluate(dequeued_t)
# While the last dequeue failed, we want to insure that it returns
# any elements that it potentially reserved to dequeue. Thus the
# next cleanup should return a single element.
results.extend(self.evaluate(cleanup_dequeue_t))
