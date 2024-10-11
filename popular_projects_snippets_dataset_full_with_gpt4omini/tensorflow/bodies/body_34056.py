# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.assertRaisesOpError("was cancelled"):
    self.evaluate(enqueue_many_op)
