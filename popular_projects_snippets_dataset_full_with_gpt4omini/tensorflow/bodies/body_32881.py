# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Unary cases.
self._check_gradient('->', ())
self._check_gradient('aaa->a', (3, 3, 3))
self._check_gradient('aabcd->ad', (3, 3, 5, 4, 4))
self._check_gradient('aabcd->add', (3, 3, 5, 4, 4))
self._check_gradient('abcd->da', (3, 5, 4, 2))
