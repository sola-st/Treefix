import re # pragma: no cover

class MethodNotAllowed405(Exception):# pragma: no cover
    def __init__(self, ip_address):# pragma: no cover
        super().__init__(f'IP {ip_address} is not allowed') # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.metadata = {'ip_address': '127.0.0.1'} # pragma: no cover
data = b'HTTP/2.0 405 Method Not Allowed' # pragma: no cover

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
