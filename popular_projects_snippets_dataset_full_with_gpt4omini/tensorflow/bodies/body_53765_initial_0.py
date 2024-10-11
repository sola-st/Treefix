tf2 = type('MockTF2', (object,), {'enabled': lambda self: True})() # pragma: no cover
self = type('MockSelf', (object,), {'skipTest': lambda self, reason: print(f'Skip test: {reason}')})() # pragma: no cover
reason = 'Test is being skipped due to tf2 being enabled.' # pragma: no cover
f = lambda self, *args, **kwargs: f'Function called with args: {args} and kwargs: {kwargs}' # pragma: no cover
args = (1, 2, 3) # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
from l3.Runtime import _l_
if tf2.enabled():
    _l_(6326)

    self.skipTest(reason)
    _l_(6325)
aux = f(self, *args, **kwargs)
_l_(6327)

exit(aux)
