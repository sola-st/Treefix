from twisted.internet import reactor # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover
from collections import deque # pragma: no cover
from typing import Dict, Tuple, Deque # pragma: no cover
from hyperframe.frame import HeadersFrame # pragma: no cover
class H2ClientProtocol: # pragma: no cover
    pass # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
reactor = reactor # pragma: no cover
settings = {} # pragma: no cover
H2ClientProtocol = H2ClientProtocol # pragma: no cover
Deferred = Deferred # pragma: no cover
Deque = deque # pragma: no cover
Dict = dict # pragma: no cover
Tuple = tuple # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
from l3.Runtime import _l_
self._reactor = reactor
_l_(17422)
self.settings = settings
_l_(17423)

# Store a dictionary which is used to get the respective
# H2ClientProtocolInstance using the  key as Tuple(scheme, hostname, port)
self._connections: Dict[Tuple, H2ClientProtocol] = {}
_l_(17424)

# Save all requests that arrive before the connection is established
self._pending_requests: Dict[Tuple, Deque[Deferred]] = {}
_l_(17425)
