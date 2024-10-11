import unittest # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._device_filters = [] # pragma: no cover
self._intra_op_parallelism_threads = 4 # pragma: no cover
self._inter_op_parallelism_threads = 2 # pragma: no cover
class StrategyConfigureTest(unittest.TestCase): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
from l3.Runtime import _l_
self._device_filters = []
_l_(10270)
self._intra_op_parallelism_threads = None
_l_(10271)
self._inter_op_parallelism_threads = None
_l_(10272)
super(StrategyConfigureTest, self).setUp()
_l_(10273)
