from unittest.mock import MagicMock # pragma: no cover

mirrored_lib = type('Mock', (object,), {'MirroredStrategyV1': MagicMock(_collective_key_base=0), 'MirroredStrategy': MagicMock(_collective_key_base=0)})() # pragma: no cover
MirroredStrategy = lambda devices: MagicMock(extended=MagicMock(_use_merge_call=lambda: False)) # pragma: no cover
devices = ['device1', 'device2'] # pragma: no cover

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
