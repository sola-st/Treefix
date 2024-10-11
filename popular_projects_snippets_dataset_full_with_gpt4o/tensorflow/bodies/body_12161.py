# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Batch matmul with broadcasting.
self._check('...ij,...jk->...ik', (1, 2, 3), (3, 5))
self._check('...ij,...jk->...ik', (2, 3), (1, 3, 5))
self._check('...ij,...jk->...ik', (5, 2, 3), (3, 5))
self._check('...ij,...jk->...ik', (2, 3), (5, 3, 5))
self._check('...ij,...jk->...ik', (3, 1, 2, 3), (1, 1, 7, 3, 5))
self._check('i...j,j...k->...ik', (2, 1, 3, 1, 3), (3, 1, 7, 5))

# Broadcasting with repeated indices.
self._check('ij,jk...k->i...', (3, 2), (2, 4, 1, 4))
self._check('ij,jk...k->...i', (3, 2), (2, 4, 5, 4))
self._check('ijj,jk...k->i...', (3, 2, 2), (2, 4, 1, 4))
self._check('i...jj,jk...k->i...', (3, 3, 1, 2, 2), (2, 4, 1, 5, 4))
# Following 2 from https://stackoverflow.com/a/19203475/1611416
self._check('...abc,...abcd->...d', (1, 1, 2, 3, 4), (5, 2, 3, 4, 6))
self._check('ab...,b->ab...', (2, 3, 1, 1, 5), (3,))
