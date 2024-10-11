# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Repeated indices.
self._check('ijj,k->ik', (2, 3, 3), (4,))
self._check('aba,a->b', (3, 4, 3), (3,))
# From https://github.com/dask/dask/pull/3412#discussion_r182413444
self._check('aab,bc->ac', (2, 2, 3), (3, 4))
self._check('aab,bcc->ac', (2, 2, 3), (3, 4, 4))
