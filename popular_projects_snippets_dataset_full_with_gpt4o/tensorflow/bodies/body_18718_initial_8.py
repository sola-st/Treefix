import numpy as np # pragma: no cover

init_ops_v2 = type('Mock', (object,), {'Identity': lambda self: 'Identity'})() # pragma: no cover
self = type('Mock', (object,), {'assertRaises': lambda self, e: np.testing.assert_raises(e), '_range_test': lambda self, op, shape, target_mean, target_max: 'range_test'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
from l3.Runtime import _l_
with self.assertRaises(ValueError):
    _l_(20214)

    shape = (3, 4, 5)
    _l_(20212)
    self._range_test(
        init_ops_v2.Identity(),
        shape=shape,
        target_mean=1. / shape[0],
        target_max=1.)
    _l_(20213)

shape = (3, 3)
_l_(20215)
self._range_test(
    init_ops_v2.Identity(),
    shape=shape,
    target_mean=1. / shape[0],
    target_max=1.)
_l_(20216)
