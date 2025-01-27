# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
get_next = self.getNext(
    dataset, requires_initialization=requires_initialization)
exit(self.getIteratorOutput(get_next))
