# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(array_ops.pad, (7, [[1, 2]]),
           'The first dimension of paddings must be the rank of inputs',
           [0, 7, 0, 0])
