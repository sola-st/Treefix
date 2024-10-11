# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check('aa->', (3, 3))
self._check('aa->a', (3, 3))
self._check('aaa->', (3, 3, 3))
self._check('aaa->a', (3, 3, 3))
self._check('aab->a', (3, 3, 4))
self._check('aabcc->a', (3, 3, 5, 4, 4))
self._check('aabcc->ac', (3, 3, 5, 4, 4))
self._check('aabcd->ad', (3, 3, 5, 4, 4))
