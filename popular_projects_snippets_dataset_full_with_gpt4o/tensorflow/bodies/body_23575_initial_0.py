self = type('MockSelf', (object,), {})() # pragma: no cover
self._trackable = type('MockTrackable', (object,), {'_tracking_metadata': 'some_metadata'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_delegate.py
from l3.Runtime import _l_
aux = self._trackable._tracking_metadata
_l_(21141)
exit(aux)
