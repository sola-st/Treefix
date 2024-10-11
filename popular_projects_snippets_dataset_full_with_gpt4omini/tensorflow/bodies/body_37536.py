# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
iterator = iter(dataset)
collective_fn(next(iterator))
# This next(iterator) should raise EOF.
collective_fn(next(iterator))
