# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.assertRaisesOpError("was cancelled"):
    self.evaluate(dequeue_up_to_op)
