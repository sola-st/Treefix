# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
for _ in range(100):
    self.assertTrue(self.evaluate(dequeued_t) in (10.0, 20.0))
