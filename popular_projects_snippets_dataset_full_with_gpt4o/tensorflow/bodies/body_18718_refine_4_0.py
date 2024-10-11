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
    def assertRaises(self, exc, callable=None, *args, **kwargs):# pragma: no cover
        if callable:# pragma: no cover
            try:# pragma: no cover
                callable(*args, **kwargs)# pragma: no cover
            except exc as e:# pragma: no cover
                return e# pragma: no cover
            raise self.failureException(f'{exc.__name__} not raised')# pragma: no cover
        return super().assertRaises(exc, callable, *args, **kwargs)# pragma: no cover
# pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max):# pragma: no cover
        array = np.ones(shape)  # Mock array returning identical elements for simplicity# pragma: no cover
        self.assertAlmostEqual(array.mean(), target_mean, delta=1e-6)# pragma: no cover
        self.assertEqual(array.max(), target_max) # pragma: no cover
init_ops_v2 = type('MockInitOpsV2', (object,), {# pragma: no cover
    'Identity': lambda: (lambda x: x)# pragma: no cover
})() # pragma: no cover
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
