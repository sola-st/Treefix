# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check_gradient('abce,badf->bcba', (1, 2, 3, 4), (2, 1, 4, 3))
