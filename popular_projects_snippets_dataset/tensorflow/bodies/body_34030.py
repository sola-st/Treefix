# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.assertRaises(errors_impl.OutOfRangeError):
    self.evaluate([dequeued_a_t, dequeued_b_t])
