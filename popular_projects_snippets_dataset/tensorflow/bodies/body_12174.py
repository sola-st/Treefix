# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check_gradient('->', ())
self._check_gradient('aaa->a', (3, 3, 3))
self._check_gradient('aabcd->ad', (3, 3, 5, 4, 4))
self._check_gradient('abcd->da', (3, 5, 4, 2))
