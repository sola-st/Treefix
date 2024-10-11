# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(array_ops.tile, ([7], 2), 'Expected multiples to be 1-D', [7, 7])
