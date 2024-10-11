# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# Will only complete after 4 enqueues complete.
results.extend(self.evaluate(deq))
