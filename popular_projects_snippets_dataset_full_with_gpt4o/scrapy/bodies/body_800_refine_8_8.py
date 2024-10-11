from unittest.mock import Mock # pragma: no cover
class MethodNotAllowed405(Exception): pass # pragma: no cover

data = b'HTTP/2.0 405 Method Not Allowed Additional Info' # pragma: no cover
self = Mock(metadata={'ip_address': '192.168.1.1'}) # pragma: no cover

from types import SimpleNamespace # pragma: no cover

data = b'HTTP/2.0 405 Method Not Allowed' # pragma: no cover
class MethodNotAllowed405(Exception):# pragma: no cover
    def __init__(self, ip_address):# pragma: no cover
        super().__init__(f"405 Method Not Allowed: {ip_address}") # pragma: no cover
self = SimpleNamespace(metadata={'ip_address': '192.168.1.1'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""Checks for edge cases where the connection to remote fails
        without raising an appropriate H2Error

        Arguments:
            data -- Data received from the remote
        """
if data.startswith(b'HTTP/2.0 405 Method Not Allowed'):
    _l_(18615)

    raise MethodNotAllowed405(self.metadata['ip_address'])
    _l_(18614)
