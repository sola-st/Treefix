import unittest # pragma: no cover
import numpy as np # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaises': unittest.TestCase.assertRaises, '_range_test': lambda self, initializer, shape, target_mean, target_max: None})() # pragma: no cover

import unittest # pragma: no cover
import numpy as np # pragma: no cover

class MockTest(unittest.TestCase):# pragma: no cover
    def _range_test(self, initializer, shape, target_mean, target_max):# pragma: no cover
        array = initializer()(shape)# pragma: no cover
        mean_diff = np.abs(np.mean(array) - target_mean)# pragma: no cover
        max_diff = np.abs(np.max(array) - target_max)# pragma: no cover
        assert mean_diff < 0.01, f'Mean diff too high: {mean_diff}'# pragma: no cover
        assert max_diff < 0.01, f'Max diff too high: {max_diff}' # pragma: no cover
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
