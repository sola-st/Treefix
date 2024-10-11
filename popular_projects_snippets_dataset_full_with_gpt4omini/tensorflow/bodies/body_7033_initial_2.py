mirrored_lib = type('Mock', (object,), { 'MirroredStrategyV1': type('Mock', (object,), { '_collective_key_base': 0 }), 'MirroredStrategy': type('Mock', (object,), { '_collective_key_base': 0 }) })() # pragma: no cover
devices = ['/device:GPU:0', '/device:GPU:1'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
from l3.Runtime import _l_
mirrored_lib.MirroredStrategyV1._collective_key_base += 100000
_l_(5423)
mirrored_lib.MirroredStrategy._collective_key_base += 100000
_l_(5424)
out = MirroredStrategy(devices)
_l_(5425)
# Stub out merge call usage.
out.extended._use_merge_call = lambda: False  # pylint: disable=protected-access
_l_(5426)  # pylint: disable=protected-access
aux = out
_l_(5427)
exit(aux)
