# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check_gradient('ij,jk...k->i...', (3, 2), (2, 4, 1, 4))
self._check_gradient('aab,b...c->a...c', (1, 1, 3), (3, 1, 1, 4))
