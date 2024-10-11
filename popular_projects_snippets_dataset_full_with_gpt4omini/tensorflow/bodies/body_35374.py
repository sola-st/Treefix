# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
results.extend(self.evaluate(dequeued_t))
self.assertEqual(3, len(results))
results.extend(self.evaluate(dequeued_t))
self.assertEqual(4, len(results))
