# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check_gradient('ba,b->', (3, 2), (3,))
self._check_gradient('ab,ab->', (3, 4), (3, 4))
self._check_gradient('abce,badf->abcd', (1, 2, 3, 4), (2, 1, 4, 3))
