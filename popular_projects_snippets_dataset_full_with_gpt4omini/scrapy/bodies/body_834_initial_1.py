from typing import Dict, Tuple, Deque # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

reactor = None # pragma: no cover
settings = {} # pragma: no cover
H2ClientProtocol = type('H2ClientProtocol', (object,), {}) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
from l3.Runtime import _l_
self._reactor = reactor
_l_(5986)
self.settings = settings
_l_(5987)

# Store a dictionary which is used to get the respective
# H2ClientProtocolInstance using the  key as Tuple(scheme, hostname, port)
self._connections: Dict[Tuple, H2ClientProtocol] = {}
_l_(5988)

# Save all requests that arrive before the connection is established
self._pending_requests: Dict[Tuple, Deque[Deferred]] = {}
_l_(5989)
