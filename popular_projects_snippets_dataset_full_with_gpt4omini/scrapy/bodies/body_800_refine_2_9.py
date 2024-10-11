from typing import Any, Dict # pragma: no cover

data = b'HTTP/2.0 405 Method Not Allowed' # pragma: no cover
class MethodNotAllowed405(Exception): pass # pragma: no cover
self = type('Mock', (object,), {'metadata': {'ip_address': '192.0.2.1'}})() # pragma: no cover

class MethodNotAllowed405(Exception): pass # pragma: no cover

data = b'HTTP/2.0 405 Method Not Allowed' # pragma: no cover
self = type('Mock', (object,), {'metadata': {'ip_address': '192.0.2.1'}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""Checks for edge cases where the connection to remote fails
        without raising an appropriate H2Error

        Arguments:
            data -- Data received from the remote
        """
if data.startswith(b'HTTP/2.0 405 Method Not Allowed'):
    _l_(7776)

    raise MethodNotAllowed405(self.metadata['ip_address'])
    _l_(7775)
