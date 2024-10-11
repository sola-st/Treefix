import unittest # pragma: no cover
import numpy as np # pragma: no cover

class MockInitializer:# pragma: no cover
    @staticmethod# pragma: no cover
    def Identity(): return np.identity# pragma: no cover
# pragma: no cover
init_ops_v2 = MockInitializer() # pragma: no cover
class MockTest(unittest.TestCase):# pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max):# pragma: no cover
        array = init_op()(shape[0])# pragma: no cover
        self.assertEqual(array.mean(), target_mean)# pragma: no cover
        self.assertEqual(array.max(), target_max) # pragma: no cover
self = MockTest() # pragma: no cover

import unittest # pragma: no cover
import numpy as np # pragma: no cover

class MockInitializer:# pragma: no cover
    @staticmethod# pragma: no cover
    def Identity(): return lambda x: np.ones(x) * (1.0 / x) # pragma: no cover
class MockTest(unittest.TestCase):# pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max):# pragma: no cover
        array = init_op()(shape[0])# pragma: no cover
        assert np.mean(array) == target_mean, f'Mean mismatch: {np.mean(array)} != {target_mean}'# pragma: no cover
        assert np.max(array) == target_max, f'Max mismatch: {np.max(array)} != {target_max}' # pragma: no cover
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
