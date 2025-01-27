# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
self._check_gradient('...->...', ())
self._check_gradient('...->', ())
self._check_gradient('->...', ())

# Tests from dask
self._check_gradient('a...a->a...', (2, 2))
self._check_gradient('a...a->', (2, 2))
self._check_gradient('a...a->...', (2, 5, 1, 2))
self._check_gradient('a...a->a...', (2, 1, 2))
self._check_gradient('a...a->a...', (2, 3, 4, 5, 2))

self._check_gradient('...ijk->...ki', (3, 4, 5))
self._check_gradient('...ijk->...ki', (1, 3, 4, 5))
self._check_gradient('...ijk->...ki', (2, 2, 3, 4, 5))
self._check_gradient('ab...cd->da...', (3, 5, 2, 3, 4, 2))
