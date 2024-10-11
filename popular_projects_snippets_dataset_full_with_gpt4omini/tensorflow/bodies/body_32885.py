# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check_gradient('ba,b->', (3, 2), (3,))
self._check_gradient('ab,ab->', (3, 4), (3, 4))
self._check_gradient('ijkm,ijln->ijmn', (2, 3, 3, 4), (2, 3, 3, 2))
self._check_gradient('abce,badf->abcd', (1, 2, 3, 4), (2, 1, 4, 3))
