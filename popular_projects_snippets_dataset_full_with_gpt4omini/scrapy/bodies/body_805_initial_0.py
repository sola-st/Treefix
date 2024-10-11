from typing import Any, Dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.metadata = {'ip_address': '192.168.1.1'} # pragma: no cover
def mock_lose_connection_with_error(connections): pass # pragma: no cover
self._lose_connection_with_error = mock_lose_connection_with_error # pragma: no cover
class RemoteTerminatedConnection: # pragma: no cover
    def __init__(self, ip_address: str, event: Any): # pragma: no cover
        self.ip_address = ip_address # pragma: no cover
        self.event = event # pragma: no cover
event = 'Connection lost due to timeout' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
self._lose_connection_with_error([
    RemoteTerminatedConnection(self.metadata['ip_address'], event)
])
_l_(9714)
