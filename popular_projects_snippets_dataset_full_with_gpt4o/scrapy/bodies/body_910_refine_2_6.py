from typing import Dict, Any, Optional, Callable # pragma: no cover
from functools import partial # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.version = (b'HTTP', 1, 1) # pragma: no cover
        self.code = 200 # pragma: no cover
 # pragma: no cover
def mock_headers_from_twisted_response(response: MockResponse) -> Dict[str, str]: # pragma: no cover
    return {'Content-Type': 'application/json'} # pragma: no cover
 # pragma: no cover
def mock_from_args(headers: Dict[str, str], url: str, body: Optional[bytes]) -> Callable: # pragma: no cover
    def response_cls(**kwargs: Any) -> Any: # pragma: no cover
        return kwargs # pragma: no cover
    return response_cls # pragma: no cover
 # pragma: no cover
def mock_to_unicode(byte_string: bytes) -> str: # pragma: no cover
    return byte_string.decode('utf-8') # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'_headers_from_twisted_response': mock_headers_from_twisted_response})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
result = { # pragma: no cover
    'txresponse': MockResponse(), # pragma: no cover
    'body': b'{}', # pragma: no cover
    'flags': ['flag1', 'flag2'], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': mock_from_args})() # pragma: no cover
to_unicode = mock_to_unicode # pragma: no cover

from typing import Dict # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.version = (b'HTTP', 1, 1) # pragma: no cover
        self.code = 200 # pragma: no cover
 # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.value = MockValue() # pragma: no cover
 # pragma: no cover
class MockValue: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.response = None # pragma: no cover
 # pragma: no cover
def mock_headers_from_twisted_response(_, response: MockResponse) -> Dict[str, str]: # pragma: no cover
    return {'Content-Type': 'application/json'} # pragma: no cover
 # pragma: no cover
def mock_from_args(**kwargs): # pragma: no cover
    return type('MockResponseClass', (object,), kwargs) # pragma: no cover
 # pragma: no cover
def mock_to_unicode(byte_string: bytes) -> str: # pragma: no cover
    return byte_string.decode('utf-8') # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'_headers_from_twisted_response': mock_headers_from_twisted_response})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
result = { # pragma: no cover
    'txresponse': MockResponse(), # pragma: no cover
    'body': b'{}', # pragma: no cover
    'flags': ['flag1', 'flag2'], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1', # pragma: no cover
    'failure': MockFailure() # pragma: no cover
} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': mock_from_args})() # pragma: no cover
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
