from twisted.web.http_headers import Headers # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

self = type('Mock', (object,), {'_headers_from_twisted_response': lambda x, y: Headers()})() # pragma: no cover
result = { # pragma: no cover
  'txresponse': type('Mock', (object,), { # pragma: no cover
    'version': (b'HTTP', 1, 1), # pragma: no cover
    'code': 200 # pragma: no cover
  })(), # pragma: no cover
  'flags': [], # pragma: no cover
  'certificate': None, # pragma: no cover
  'ip_address': '127.0.0.1', # pragma: no cover
  'body': b'body content', # pragma: no cover
  'failure': type('Mock', (object,), {'value': type('Mock', (object,), {'response': None})()})() # pragma: no cover
} # pragma: no cover
responsettypes = type('Mock', (object,), {'from_args': lambda headers, url, body: type('Mock', (object,), {})}) # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') # pragma: no cover

from twisted.web.http_headers import Headers # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.version = (b'HTTP', 1, 1) # pragma: no cover
        self.code = 200 # pragma: no cover
 # pragma: no cover
def mock_headers_from_twisted_response(response: MockResponse) -> Headers: # pragma: no cover
    return Headers({b'Content-Type': [b'application/json']}) # pragma: no cover
 # pragma: no cover
def response_class(*args,**kwargs): return type('Response', (object,), kwargs) # pragma: no cover
responsetypes = type('MockResponseTypes', (object,), { # pragma: no cover
    'from_args': lambda **kwargs: response_class(**kwargs) # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
def mock_to_unicode(string: bytes) -> str: # pragma: no cover
    return string.decode('utf-8') if isinstance(string, bytes) else str(string) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'_headers_from_twisted_response': mock_headers_from_twisted_response})() # pragma: no cover
 # pragma: no cover
result = { # pragma: no cover
    'txresponse': MockResponse(), # pragma: no cover
    'body': b'{}', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
 # pragma: no cover
url = 'http://example.com' # pragma: no cover
 # pragma: no cover
to_unicode = mock_to_unicode # pragma: no cover

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
