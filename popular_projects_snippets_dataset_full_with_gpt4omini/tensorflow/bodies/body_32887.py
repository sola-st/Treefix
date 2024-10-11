# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Repeated indices.
self._check_gradient('aba,a->b', (3, 4, 3), (3,))
self._check_gradient('ijj,k->ik', (2, 3, 3), (4,))
self._check_gradient('ill,k->ik', (2, 3, 3), (4,))
# From https://github.com/dask/dask/pull/3412#discussion_r182413444
self._check_gradient('aab,bc->ac', (1, 1, 3), (3, 4))
self._check_gradient('aab,bcc->ac', (2, 2, 3), (3, 4, 4))
