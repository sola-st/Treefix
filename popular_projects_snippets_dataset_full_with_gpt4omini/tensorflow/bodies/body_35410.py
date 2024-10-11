# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
enq_done.append(False)
# This will fill the queue and then block until enough dequeues happen.
self.evaluate(enq)
enq_done.append(True)
