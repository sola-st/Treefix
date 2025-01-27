# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check('a', (3,))
self._check('aa', (3, 3))
self._check('ab->', (3, 3))
self._check('ab->ab', (3, 3))
self._check('abc->b', (3, 4, 5))
self._check('abc->ca', (3, 4, 5))
self._check('abc->cab', (3, 4, 5))

# Empty cases.
self._check('', ())
self._check('->', ())

# Repeated indices cases.
self._check('aa->', (3, 3))
self._check('aa->a', (3, 3))
self._check('aaa->', (3, 3, 3))
self._check('aaa->a', (3, 3, 3))
self._check('aab->a', (3, 3, 4))
self._check('aabcc->a', (3, 3, 5, 4, 4))
self._check('aabcc->ac', (3, 3, 5, 4, 4))
self._check('aabcd->ad', (3, 3, 5, 4, 4))
