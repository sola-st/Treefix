import unittest # pragma: no cover

self = type('MockSelf', (unittest.TestCase,), {# pragma: no cover
    'assertRaises': unittest.TestCase().assertRaises,# pragma: no cover
    '_range_test': lambda self, op, shape, target_mean, target_max: None# pragma: no cover
})() # pragma: no cover
init_ops_v2 = type('MockInitOpsV2', (), {# pragma: no cover
    'Identity': type('Identity', (), {})# pragma: no cover
})() # pragma: no cover

import unittest # pragma: no cover
import numpy as np # pragma: no cover

class MockTest(unittest.TestCase):# pragma: no cover
    def _range_test(self, initializer, shape, target_mean, target_max):# pragma: no cover
        array = initializer# pragma: no cover
        if callable(initializer):# pragma: no cover
            array = np.full(shape, target_mean)# pragma: no cover
        computed_mean = array.mean()# pragma: no cover
        computed_max = array.max()# pragma: no cover
        if computed_mean != target_mean or computed_max > target_max:# pragma: no cover
            raise ValueError('Range test failed') # pragma: no cover
self = MockTest() # pragma: no cover

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
