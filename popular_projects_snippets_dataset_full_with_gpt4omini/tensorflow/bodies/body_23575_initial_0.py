from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self._trackable = SimpleNamespace() # pragma: no cover
self._trackable._tracking_metadata = 'mock_metadata' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_delegate.py
from l3.Runtime import _l_
aux = self._trackable._tracking_metadata
_l_(8730)
exit(aux)
