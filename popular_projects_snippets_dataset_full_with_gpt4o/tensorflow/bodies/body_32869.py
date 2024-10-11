# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Broadcasting with repeated indices.
self._check('ij,jk...k->i...', (3, 2), (2, 4, 1, 4))
self._check('ij,jk...k->...i', (3, 2), (2, 4, 5, 4))
self._check('ijj,jk...k->i...', (3, 2, 2), (2, 4, 1, 4))
self._check('i...jj,jk...k->i...', (3, 3, 1, 2, 2), (2, 4, 1, 5, 4))
