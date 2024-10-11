import types # pragma: no cover

tf2 = type('Mock', (object,), {'enabled': lambda: True}) # pragma: no cover
self = type('Mock', (object,), {'skipTest': lambda reason: None}) # pragma: no cover
reason = 'Test skipped for a specific reason' # pragma: no cover
f = lambda self, *args, **kwargs: 0 # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
from l3.Runtime import _l_
if tf2.enabled():
    _l_(18789)

    self.skipTest(reason)
    _l_(18788)
aux = f(self, *args, **kwargs)
_l_(18790)

exit(aux)
