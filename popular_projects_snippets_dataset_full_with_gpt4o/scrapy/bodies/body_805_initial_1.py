from typing import Any, Dict # pragma: no cover
class RemoteTerminatedConnection: # pragma: no cover
    def __init__(self, ip_address: str, event: Any): # pragma: no cover
        self.ip_address = ip_address # pragma: no cover
        self.event = event # pragma: no cover

event = 'disconnection_reason' # pragma: no cover
self = type('Mock', (object,), { 'metadata': { 'ip_address': '192.168.1.1' }, '_lose_connection_with_error': lambda self, x: None })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
self._lose_connection_with_error([
    RemoteTerminatedConnection(self.metadata['ip_address'], event)
])
_l_(20902)
