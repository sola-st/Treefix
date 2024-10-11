# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
self._check('->', ())
self._check('ab->', (3, 3))
self._check('ab->ab', (3, 3))
self._check('abc->b', (3, 4, 5))
self._check('abc->ca', (3, 4, 5))
self._check('abc->cab', (3, 4, 5))
