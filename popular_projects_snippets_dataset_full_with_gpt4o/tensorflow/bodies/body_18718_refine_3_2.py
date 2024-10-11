import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaises': unittest.TestCase().assertRaises, '_range_test': lambda self, init, shape, target_mean, target_max: print(f'Range test with {init}, shape={shape}, target_mean={target_mean}, target_max={target_max}')})() # pragma: no cover

import unittest # pragma: no cover
import numpy as np # pragma: no cover

class MockInitializer:# pragma: no cover
    @staticmethod# pragma: no cover
    def Identity(): return np.identity# pragma: no cover
# pragma: no cover
init_ops_v2 = MockInitializer() # pragma: no cover
class MockTest(unittest.TestCase):# pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max):# pragma: no cover
        array = init_op()(shape[0]) if callable(init_op) else init_op# pragma: no cover
        assert array.mean() == target_mean, f"Expected mean: {target_mean}, but got: {array.mean()}"# pragma: no cover
        assert array.max() == target_max, f"Expected max: {target_max}, but got: {array.max()}"# pragma: no cover
# pragma: no cover
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
