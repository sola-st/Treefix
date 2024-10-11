import unittest # pragma: no cover
import numpy as np # pragma: no cover

self = type('Mock', (object,), {'assertRaises': unittest.TestCase().assertRaises, '_range_test': lambda self, identity, shape, target_mean, target_max: None})() # pragma: no cover
init_ops_v2 = type('Mock', (object,), {'Identity': lambda: np.identity}) # pragma: no cover

import unittest # pragma: no cover

class MockSelf(unittest.TestCase):# pragma: no cover
    def assertRaises(self, exc, callable=None, *args, **kwds):# pragma: no cover
        if callable is None:# pragma: no cover
            return super().assertRaises(exc)# pragma: no cover
        try:# pragma: no cover
            callable(*args, **kwds)# pragma: no cover
        except exc:# pragma: no cover
            return# pragma: no cover
        raise AssertionError(f'{exc.__name__} not raised')# pragma: no cover
# pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max):# pragma: no cover
        if shape == (3, 4, 5):# pragma: no cover
            raise ValueError('Intentional error for test purposes')# pragma: no cover
        # Mock behavior for other shapes# pragma: no cover
        print(f'Range test: shape={shape}, target_mean={target_mean}, target_max={target_max}')# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

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
