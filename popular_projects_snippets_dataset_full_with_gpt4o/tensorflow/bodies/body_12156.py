# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check('...->', ())
self._check('...ijk->...ki', (3, 4, 5))
self._check('...ijk->...ki', (1, 3, 4, 5))
self._check('...ijk->...ki', (2, 2, 3, 4, 5))
self._check('...ij->...ji', (5, 2, 3))  # batch matrix transpose
self._check('...ij->...', (5, 2, 3))  # batch sum

self._check('...->...', ())
self._check('->...', ())

# Repeated indices.
self._check('i...ii->...i', (3, 2, 3, 3))
self._check('i...i->i...', (2, 2))
self._check('i...i->', (2, 2))
self._check('i...i->...', (2, 5, 1, 2))
self._check('i...i->i...', (2, 1, 2))
self._check('i...i->i...', (2, 3, 4, 5, 2))
