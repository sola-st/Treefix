self = type('Mock', (object,), {'_lose_connection_with_error': lambda x: None, 'metadata': {'ip_address': '192.168.0.1'}})() # pragma: no cover
event = 'Connection lost due to error' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
self._lose_connection_with_error([
    RemoteTerminatedConnection(self.metadata['ip_address'], event)
])
_l_(20902)
