# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check_gradient('...ij,...jk->...ik', (3, 2), (2, 4))
self._check_gradient('ij...,jk...->ik...', (3, 2, 1), (2, 4))
self._check_gradient('...ij,...jk->...ik', (3, 1, 3, 2), (1, 5, 2, 4))
self._check_gradient('ij,jk...k->i...', (3, 2), (2, 4, 1, 4))
self._check_gradient('aab,b...c->a...c', (1, 1, 3), (3, 1, 1, 4))
# Tests from dask.
self._check_gradient('...i,...j,...k->...ijk', (1, 4, 1, 2), (5, 1, 1, 3),
                     (1, 1, 1, 1, 9))
self._check_gradient('...i,...j,...k->...ijk', (1,), (1,), (1,))
