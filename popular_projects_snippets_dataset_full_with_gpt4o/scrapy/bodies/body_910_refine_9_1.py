from typing import Any # pragma: no cover
class MockFailure: pass # pragma: no cover

self = type('Mock', (object,), {'_headers_from_twisted_response': lambda self, txresponse: {'Content-Type': 'text/html'}})() # pragma: no cover
result = {'txresponse': type('Mock', (object,), {'version': (1, 1, 1), 'code': 200})(), 'body': b'<html></html>', 'flags': [], 'certificate': None, 'ip_address': '127.0.0.1', 'failure': None} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': lambda headers, url, body: type('MockResponse', (object,), {'__call__': lambda self, *args, **kwargs: 'Response Object'})})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda x: str(x) # pragma: no cover

from typing import Any, Dict, NamedTuple # pragma: no cover

class MockHeadersFromTwistedResponse: # pragma: no cover
    def __call__(self, response: Any) -> Dict[str, str]: # pragma: no cover
        return {'Content-Type': 'text/html'} # pragma: no cover
 # pragma: no cover
class MockResponseClass(NamedTuple): # pragma: no cover
    url: str # pragma: no cover
    status: int # pragma: no cover
    headers: Dict[str, str] # pragma: no cover
    body: bytes # pragma: no cover
    flags: list # pragma: no cover
    certificate: Any # pragma: no cover
    ip_address: str # pragma: no cover
    protocol: str # pragma: no cover
 # pragma: no cover
class MockResponseTypes: # pragma: no cover
    def from_args(self, headers: Dict[str, str], url: str, body: bytes) -> MockResponseClass: # pragma: no cover
        return MockResponseClass(url=url, status=200, headers=headers, body=body, flags=[], certificate=None, ip_address='127.0.0.1', protocol='HTTP/1.1') # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'_headers_from_twisted_response': MockHeadersFromTwistedResponse()})() # pragma: no cover
 # pragma: no cover
url = 'http://example.com' # pragma: no cover
 # pragma: no cover
result = { # pragma: no cover
    'txresponse': type('MockResponse', (object,), { # pragma: no cover
        'version': (b'HTTP', 1, 1), # pragma: no cover
        'code': 200 # pragma: no cover
    })(), # pragma: no cover
    'body': b'<html></html>', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': type('MockFailure', (object,), { # pragma: no cover
        'value': type('MockValue', (object,), { # pragma: no cover
            'response': None # pragma: no cover
        })() # pragma: no cover
    })() # pragma: no cover
} # pragma: no cover
 # pragma: no cover
responsetypes = MockResponseTypes() # pragma: no cover
 # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') if isinstance(x, bytes) else str(x) # pragma: no cover

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
