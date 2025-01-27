# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check('ba,b->', (3, 2), (3,))
self._check('ab,ab->', (3, 4), (3, 4))
self._check('abce,badf->abcd', (1, 2, 3, 4), (2, 1, 4, 3))
