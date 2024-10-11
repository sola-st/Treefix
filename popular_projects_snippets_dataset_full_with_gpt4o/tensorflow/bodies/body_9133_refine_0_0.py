self = type('Mock', (object,), {'_device_filters': [], '_intra_op_parallelism_threads': None, '_inter_op_parallelism_threads': None})() # pragma: no cover
StrategyConfigureTest = type('StrategyConfigureTest', (object,), {'setUp': lambda self: None}) # pragma: no cover

class StrategyConfigureTestBase:# pragma: no cover
    def setUp(self):# pragma: no cover
        pass # pragma: no cover
self = type('Mock', (object,), {'_device_filters': [], '_intra_op_parallelism_threads': None, '_inter_op_parallelism_threads': None})() # pragma: no cover
StrategyConfigureTest = type('StrategyConfigureTest', (StrategyConfigureTestBase,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
from l3.Runtime import _l_
self._device_filters = []
_l_(22463)
self._intra_op_parallelism_threads = None
_l_(22464)
self._inter_op_parallelism_threads = None
_l_(22465)
super(StrategyConfigureTest, self).setUp()
_l_(22466)
