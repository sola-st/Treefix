import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaises': unittest.TestCase().assertRaises, '_range_test': lambda self, init, shape, target_mean, target_max: print(f'Range test with {init}, shape={shape}, target_mean={target_mean}, target_max={target_max}')})() # pragma: no cover

import unittest # pragma: no cover
import numpy as np # pragma: no cover

class init_ops_v2:# pragma: no cover
    @staticmethod# pragma: no cover
    def Identity():# pragma: no cover
        return lambda: np.identity # pragma: no cover
class Mock(unittest.TestCase):# pragma: no cover
    def _range_test(self, init, shape, target_mean, target_max):# pragma: no cover
        array = init()(shape[0])# pragma: no cover
        self.assertAlmostEqual(array.mean(), target_mean)# pragma: no cover
        self.assertEqual(array.max(), target_max) # pragma: no cover
self = Mock() # pragma: no cover

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
