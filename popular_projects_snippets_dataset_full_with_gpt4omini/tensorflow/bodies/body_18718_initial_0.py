import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._range_test = lambda init, shape, target_mean, target_max: None # pragma: no cover
class MockIdentity: pass # pragma: no cover
init_ops_v2 = Mock() # pragma: no cover
init_ops_v2.Identity = MockIdentity # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
from l3.Runtime import _l_
with self.assertRaises(ValueError):
    _l_(7232)

    shape = (3, 4, 5)
    _l_(7230)
    self._range_test(
        init_ops_v2.Identity(),
        shape=shape,
        target_mean=1. / shape[0],
        target_max=1.)
    _l_(7231)

shape = (3, 3)
_l_(7233)
self._range_test(
    init_ops_v2.Identity(),
    shape=shape,
    target_mean=1. / shape[0],
    target_max=1.)
_l_(7234)
