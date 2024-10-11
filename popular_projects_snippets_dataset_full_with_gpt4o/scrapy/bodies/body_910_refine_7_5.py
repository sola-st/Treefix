from typing import Any, Optional, Dict # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockHeadersFromTwistedResponse: # pragma: no cover
    def __call__(self, txresponse: Any) -> Dict[str, Any]: # pragma: no cover
        return {'Content-Type': 'text/html', 'Server': 'Twisted'} # pragma: no cover
 # pragma: no cover
MockResponsetypes = type( # pragma: no cover
    'MockResponsetypes', # pragma: no cover
    (object,), # pragma: no cover
    {'from_args': lambda headers, url, body: SimpleNamespace( # pragma: no cover
        url=url, status=None, headers=headers, body=body, # pragma: no cover
        flags=None, certificate=None, ip_address=None, protocol=None # pragma: no cover
    )} # pragma: no cover
) # pragma: no cover
 # pragma: no cover
def mock_to_unicode(value: Any) -> str: # pragma: no cover
    return str(value) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'_headers_from_twisted_response': MockHeadersFromTwistedResponse()})() # pragma: no cover
 # pragma: no cover
url = 'https://example.com' # pragma: no cover
 # pragma: no cover
result = { # pragma: no cover
    'txresponse': SimpleNamespace( # pragma: no cover
        version=(b'HTTP', 1, 1), # pragma: no cover
        code=200 # pragma: no cover
    ), # pragma: no cover
    'body': b'<html></html>', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1' # pragma: no cover
} # pragma: no cover
 # pragma: no cover
responsetypes = MockResponsetypes # pragma: no cover
 # pragma: no cover
to_unicode = mock_to_unicode # pragma: no cover

from typing import Dict, Any, Tuple # pragma: no cover

class MockSelf: # pragma: no cover
    def _headers_from_twisted_response(self, response: Any) -> Dict[str, str]: # pragma: no cover
        return {'Content-Type': 'text/html'} # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
class MockTxResponse: # pragma: no cover
    version: Tuple[bytes, int, int] = (b'HTTP', 1, 1) # pragma: no cover
    code: int = 200 # pragma: no cover
 # pragma: no cover
result = { # pragma: no cover
    'txresponse': MockTxResponse(), # pragma: no cover
    'body': b'<html></html>', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
 # pragma: no cover
class MockResponseTypes: # pragma: no cover
    def from_args(self, **kwargs) -> 'ResponseClass': # pragma: no cover
        class ResponseClass: # pragma: no cover
            def __init__(self, **kwargs): # pragma: no cover
                self.__dict__.update(kwargs) # pragma: no cover
        return ResponseClass(**kwargs) # pragma: no cover
 # pragma: no cover
responsetypes = MockResponseTypes() # pragma: no cover
 # pragma: no cover
url = 'http://example.com' # pragma: no cover
 # pragma: no cover
def to_unicode(value: bytes) -> str: # pragma: no cover
    return value.decode('utf-8') # pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
headers = self._headers_from_twisted_response(result["txresponse"])
_l_(18561)
respcls = responsetypes.from_args(headers=headers, url=url, body=result["body"])
_l_(18562)
try:
    _l_(18567)

    version = result["txresponse"].version
    _l_(18563)
    protocol = f"{to_unicode(version[0])}/{version[1]}.{version[2]}"
    _l_(18564)
except (AttributeError, TypeError, IndexError):
    _l_(18566)

    protocol = None
    _l_(18565)
response = respcls(
    url=url,
    status=int(result["txresponse"].code),
    headers=headers,
    body=result["body"],
    flags=result["flags"],
    certificate=result["certificate"],
    ip_address=result["ip_address"],
    protocol=protocol,
)
_l_(18568)
if result.get("failure"):
    _l_(18571)

    result["failure"].value.response = response
    _l_(18569)
    aux = result["failure"]
    _l_(18570)
    exit(aux)
aux = response
_l_(18572)
exit(aux)
