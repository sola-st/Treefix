# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/svd_op_test.py
from l3.Runtime import _l_
for batch_dims in [(), (3,)] + [(3, 2)] * (n < 10):
    _l_(21616)

    self._testSvdCorrectness(dtype, batch_dims + (n, n))
    _l_(21613)
    self._testSvdCorrectness(dtype, batch_dims + (2 * n, n))
    _l_(21614)
    self._testSvdCorrectness(dtype, batch_dims + (n, 2 * n))
    _l_(21615)
