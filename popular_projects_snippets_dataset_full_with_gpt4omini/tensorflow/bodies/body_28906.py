# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
tuple_elem = (constant_op.constant([1, 2, 3]), dataset_ops.Dataset.range(3))
self._testInvalidElement(tuple_elem)
