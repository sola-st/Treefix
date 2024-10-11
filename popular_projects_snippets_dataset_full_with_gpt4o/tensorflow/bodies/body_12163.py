# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check('ijk,ijl,ikl->i', (1, 2, 3), (1, 2, 4), (1, 3, 4))
self._check('i,ijk,j->k', (1,), (1, 2, 4), (2,))
self._check('ij,ij,jk,kl->il', (1, 2), (1, 2), (2, 3), (3, 4))
# Tests from dask.
self._check('a,b,c', (5,), (7,), (9,))
self._check('ab,ab,c->c', (5, 6), (5, 6), (2,))
