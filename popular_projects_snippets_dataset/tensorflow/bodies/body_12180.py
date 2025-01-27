# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check_gradient('aab,bc->ac', (0, 0, 10), (10, 10))
self._check_gradient('aab,bc->ac', (1, 1, 0), (0, 10))
self._check_gradient('aaab,bc->c', (0, 0, 0, 3), (3, 4))
