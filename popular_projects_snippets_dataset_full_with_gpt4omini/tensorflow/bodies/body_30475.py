# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(
    array_ops.reshape, (7, 1),
    'sizes input must be 1-D', [7],
    lenient=[5, 6],
    strict=[])
