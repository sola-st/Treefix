# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# The enqueue_ops should run after the dequeue op has blocked.
# TODO(mrry): Figure out how to do this without sleeping.
time.sleep(0.1)
for enqueue_op in enqueue_ops:
    self.evaluate(enqueue_op)
