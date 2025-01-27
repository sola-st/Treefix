# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# The enqueue_op should run after the dequeue op has blocked.
# TODO(mrry): Figure out how to do this without sleeping.
time.sleep(0.1)
self.evaluate(enqueue_op)
