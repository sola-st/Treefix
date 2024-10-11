from typing import Any, Tuple # pragma: no cover

n = 5 # pragma: no cover
dtype = 'float32' # pragma: no cover
self = type('Mock', (object,), {'_testSvdCorrectness': lambda self, dtype, shape: print(f'Testing SVD for dtype={dtype}, shape={shape}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/svd_op_test.py
from l3.Runtime import _l_
for batch_dims in [(), (3,)] + [(3, 2)] * (n < 10):
    _l_(9254)

    self._testSvdCorrectness(dtype, batch_dims + (n, n))
    _l_(9251)
    self._testSvdCorrectness(dtype, batch_dims + (2 * n, n))
    _l_(9252)
    self._testSvdCorrectness(dtype, batch_dims + (n, 2 * n))
    _l_(9253)
