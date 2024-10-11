# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(sparse_ops.sparse_to_dense, (1, 4, 7),
           'output_shape must be rank 1', [0, 7, 0, 0])
