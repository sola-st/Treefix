import types # pragma: no cover

mirrored_lib = types.ModuleType('mirrored_lib') # pragma: no cover
mirrored_lib.MirroredStrategyV1 = type('MirroredStrategyV1', (object,), {'_collective_key_base': 0}) # pragma: no cover
mirrored_lib.MirroredStrategy = type('MirroredStrategy', (object,), {'_collective_key_base': 0}) # pragma: no cover
MirroredStrategy = type('MirroredStrategy', (object,), {'extended': lambda self: type('extended', (object,), {'_use_merge_call': None})()}) # pragma: no cover
devices = ['/device:GPU:0', '/device:GPU:1'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
from l3.Runtime import _l_
mirrored_lib.MirroredStrategyV1._collective_key_base += 100000
_l_(17053)
mirrored_lib.MirroredStrategy._collective_key_base += 100000
_l_(17054)
out = MirroredStrategy(devices)
_l_(17055)
# Stub out merge call usage.
out.extended._use_merge_call = lambda: False  # pylint: disable=protected-access
_l_(17056)  # pylint: disable=protected-access
aux = out
_l_(17057)
exit(aux)
