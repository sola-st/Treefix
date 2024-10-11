# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Batch matmul with broadcasting.
self._check('...ij,...jk->...ik', (1, 2, 3), (3, 5))
self._check('...ij,...jk->...ik', (2, 3), (1, 3, 5))
self._check('...ij,...jk->...ik', (5, 2, 3), (3, 5))
self._check('...ij,...jk->...ik', (2, 3), (5, 3, 5))
self._check('...ij,...jk->...ik', (3, 1, 2, 3), (1, 1, 7, 3, 5))
self._check('i...j,j...k->...ik', (2, 1, 3, 1, 3), (3, 1, 7, 5))
# Following 2 from https://stackoverflow.com/a/19203475/1611416
self._check('...abc,...abcd->...d', (1, 1, 2, 3, 4), (5, 2, 3, 4, 6))
self._check('ab...,b->ab...', (2, 3, 1, 1, 5), (3,))
self._check('i...j,j...k->i...k', (3, 1, 2, 2), (2, 2, 3, 1, 4))
