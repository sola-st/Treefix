class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._headers_from_twisted_response = lambda response: {'Content-Type': 'application/json'} # pragma: no cover
result = { 'txresponse': { 'version': [1, 1, 0], 'code': 200 }, 'body': '{}', 'flags': None, 'certificate': None, 'ip_address': '127.0.0.1', 'failure': None } # pragma: no cover
class ResponseTypes: pass # pragma: no cover
responsetypes = ResponseTypes() # pragma: no cover
responsetypes.from_args = lambda headers, url, body: lambda url, status, headers, body, flags, certificate, ip_address, protocol: {'url': url, 'status': status, 'headers': headers, 'body': body, 'flags': flags, 'certificate': certificate, 'ip_address': ip_address, 'protocol': protocol} # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = str # pragma: no cover

from typing import Dict, Any, Optional # pragma: no cover

class MockTXResponse: pass # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._headers_from_twisted_response = lambda response: {'Content-Type': 'application/json'} # pragma: no cover
txresponse = MockTXResponse() # pragma: no cover
txresponse.version = [1, 1, 0] # pragma: no cover
txresponse.code = 200 # pragma: no cover
result = { # pragma: no cover
    'txresponse': txresponse, # pragma: no cover
    'body': '{"key": "value"}', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '192.0.2.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
class MockResponseType: pass # pragma: no cover
def mock_from_args(headers, url, body): return MockResponseType() # pragma: no cover
responsetypes = type('MockResponseTypes', (object,), {'from_args': staticmethod(mock_from_args)})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = str # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
headers = self._headers_from_twisted_response(result["txresponse"])
_l_(7678)
respcls = responsetypes.from_args(headers=headers, url=url, body=result["body"])
_l_(7679)
try:
    _l_(7684)

    version = result["txresponse"].version
    _l_(7680)
    protocol = f"{to_unicode(version[0])}/{version[1]}.{version[2]}"
    _l_(7681)
except (AttributeError, TypeError, IndexError):
    _l_(7683)

    protocol = None
    _l_(7682)
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
_l_(7685)
if result.get("failure"):
    _l_(7688)

    result["failure"].value.response = response
    _l_(7686)
    aux = result["failure"]
    _l_(7687)
    exit(aux)
aux = response
_l_(7689)
exit(aux)
