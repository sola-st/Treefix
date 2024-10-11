import sys # pragma: no cover

class Mock(object): pass # pragma: no cover
self = Mock() # pragma: no cover
self._fed_devices = ['device1', 'device2', 'device3'] # pragma: no cover
worker_index = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
from l3.Runtime import _l_
aux = self._fed_devices[worker_index]
_l_(21609)
exit(aux)
