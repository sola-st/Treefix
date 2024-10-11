# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check_gradient('aab,bc->ac', (0, 0, 10), (10, 10))
self._check_gradient('aab,bc->ac', (1, 1, 0), (0, 10))
self._check_gradient('aaab,bc->c', (0, 0, 0, 3), (3, 4))
