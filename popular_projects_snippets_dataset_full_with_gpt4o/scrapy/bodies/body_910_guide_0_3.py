import twisted.web.client # pragma: no cover
from twisted.internet import defer # pragma: no cover

class MockTxresponse: # pragma: no cover
    version = None # pragma: no cover
    code = 200 # pragma: no cover
def mock_headers_from_twisted_response(txresponse): # pragma: no cover
    return {'Content-Type': 'text/html'} # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.value = MockFailureValue() # pragma: no cover
class MockFailureValue: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.response = None # pragma: no cover
class MockResponseType: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_args(headers, url, body): # pragma: no cover
        return MockResponse(url, headers, body) # pragma: no cover
class MockResponse: # pragma: no cover
    def __init__(self, url, headers, body): # pragma: no cover
        self.url = url # pragma: no cover
        self.headers = headers # pragma: no cover
        self.body = body # pragma: no cover
        self.status = None # pragma: no cover
        self.flags = None # pragma: no cover
        self.certificate = None # pragma: no cover
        self.ip_address = None # pragma: no cover
        self.protocol = None # pragma: no cover
def to_unicode(version): # pragma: no cover
    return str(version) # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_headers_from_twisted_response': mock_headers_from_twisted_response # pragma: no cover
})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
result = { # pragma: no cover
    'txresponse': MockTxresponse(), # pragma: no cover
    'body': b'Example body', # pragma: no cover
    'flags': None, # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': None, # pragma: no cover
    'failure': MockFailure() # pragma: no cover
} # pragma: no cover
responsetypes = MockResponseType # pragma: no cover

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
