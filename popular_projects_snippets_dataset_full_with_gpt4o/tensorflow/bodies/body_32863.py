# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Unary cases with ellipsis.
# Edge cases.
self._check('...->...', ())
self._check('...->', ())
self._check('->...', ())

# Tests from dask
self._check('a...a->a...', (2, 2))
self._check('a...a->', (2, 2))
self._check('a...a->...', (2, 5, 1, 2))
self._check('a...a->a...', (2, 1, 2))
self._check('a...a->a...', (2, 3, 4, 5, 2))

# Regular cases.
self._check('...ijk->...ki', (3, 4, 5))
self._check('...ijk->...ki', (1, 3, 4, 5))
self._check('...ijk->...ki', (2, 2, 3, 4, 5))

# Repeated indices.
self._check('i...ii->...i', (3, 2, 3, 3))
