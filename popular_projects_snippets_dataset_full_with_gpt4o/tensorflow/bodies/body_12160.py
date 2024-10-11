# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Batch matmul with ellipsis but without broadcasting.
self._check('...mk,...kn->...mn', (5, 1, 2, 3), (5, 1, 3, 4))
# Empty batch dimensions.
self._check('...mk,...kn->...mn', (2, 3), (3, 4))
# Tensor contraction with transpose.
self._check('...ija,aijb...->ba...ij', (1, 2, 2, 3, 1), (1, 2, 3, 4, 1, 2))
# Output subscripts may omit ellipsis when batch shape is empty.
self._check('...mk,...kn->mn', (2, 3), (3, 4))
self._check('...mk,kn->mn', (2, 3), (3, 4))
self._check('mk,...kn->mn', (2, 3), (3, 4))
self._check('...,...->...', (2, 3), (2, 3))  # hadamard product
self._check('...i,...j->...ij', (5, 2), (5, 3))  # outer product
