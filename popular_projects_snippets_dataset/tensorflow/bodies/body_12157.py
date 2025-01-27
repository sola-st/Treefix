# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Binary cases in XLA mode must have either (a) each index appearing exactly
# once in both the inputs (batch or contraction index), or (b) appearing
# exactly once in an input and in the output (free index).
self._check(',->', (), ())
self._check('a,a->', (3,), (3,))
self._check('a,a->a', (3,), (3,))
self._check('ab,b->a', (3, 4), (4,))
self._check('ab,ab->', (3, 4), (3, 4))
self._check('ab,bc->ac', (3, 4), (4, 5))
self._check('nij,jk->nik', (5, 2, 3), (3, 4))
self._check('abc,bad->abcd', (1, 2, 3), (2, 1, 4))
# Based on https://github.com/google/jax/issues/37#issuecomment-448572187
self._check('sa,shb->shab', (2, 1), (2, 3, 4))
# Infer the output subscripts.
self._check('ab,b', (3, 4), (4,))
self._check('cab,b', (1, 3, 4), (4,))
