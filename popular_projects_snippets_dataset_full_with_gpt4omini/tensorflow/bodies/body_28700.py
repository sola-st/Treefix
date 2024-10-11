# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
get_next = self.getNext(dataset_fn())
for _ in range(100):
    self.evaluate(get_next())
