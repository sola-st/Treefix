# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check_gradient('...ij,...jk->...ik', (3, 2), (2, 4))
self._check_gradient('ij...,jk...->ik...', (3, 2, 1), (2, 4))
self._check_gradient('...ij,...jk->...ik', (3, 1, 3, 2), (1, 5, 2, 4))
self._check_gradient('i...j,j...k->i...k', (3, 1, 2, 2), (2, 2, 3, 1, 4))
