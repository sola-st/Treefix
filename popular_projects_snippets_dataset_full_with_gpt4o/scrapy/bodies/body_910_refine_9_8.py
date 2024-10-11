from typing import Any # pragma: no cover
class MockFailure: pass # pragma: no cover

self = type('Mock', (object,), {'_headers_from_twisted_response': lambda self, txresponse: {'Content-Type': 'text/html'}})() # pragma: no cover
result = {'txresponse': type('Mock', (object,), {'version': (1, 1, 1), 'code': 200})(), 'body': b'<html></html>', 'flags': [], 'certificate': None, 'ip_address': '127.0.0.1', 'failure': None} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': lambda headers, url, body: type('MockResponse', (object,), {'__call__': lambda self, *args, **kwargs: 'Response Object'})})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda x: str(x) # pragma: no cover

from typing import Any, Dict, Optional, Union # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockSelf: # pragma: no cover
    def _headers_from_twisted_response(self, response: Any) -> Dict[str, str]: # pragma: no cover
        return {'Content-Type': 'text/html'} # pragma: no cover
 # pragma: no cover
class MockResponseTypes: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_args(headers: Optional[Dict[str, str]], url: str, body: Union[bytes, str]): # pragma: no cover
        return lambda **kwargs: SimpleNamespace(**kwargs) # pragma: no cover
 # pragma: no cover
def to_unicode(value: Union[bytes, str]) -> str: # pragma: no cover
    return value.decode('utf-8') if isinstance(value, bytes) else str(value) # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
url = 'http://example.com' # pragma: no cover
result = { # pragma: no cover
    'txresponse': SimpleNamespace(version=(b'HTTP', 1, 1), code=200), # pragma: no cover
    'body': b'<html></html>', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
responsetypes = MockResponseTypes # pragma: no cover
to_unicode = to_unicode # pragma: no cover

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
