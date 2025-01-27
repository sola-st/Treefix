# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
results.extend(self.evaluate(dequeued_t))
self.assertEqual(3, len(results))
# min_after_dequeue is 2, we ask for 3 elements, and we end up only
# getting the remaining 1.
results.extend(self.evaluate(dequeued_t))
self.assertEqual(4, len(results))
