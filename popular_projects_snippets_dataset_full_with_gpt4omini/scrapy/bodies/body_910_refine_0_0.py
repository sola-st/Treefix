from typing import Dict, Any, Optional, Union # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._headers_from_twisted_response = lambda response: {'Content-Type': 'application/json'} # pragma: no cover
result = { # pragma: no cover
    'txresponse': Mock(), # pragma: no cover
    'body': '{"key": "value"}', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '192.0.2.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
result['txresponse'].version = (1, 1, 1) # pragma: no cover
result['txresponse'].code = 200 # pragma: no cover
url = 'http://example.com' # pragma: no cover
class MockResponseType: pass # pragma: no cover
responsetypes = type('MockResponseTypes', (object,), {'from_args': lambda *args, **kwargs: MockResponseType()}) # pragma: no cover
to_unicode = str # pragma: no cover

from typing import Dict, Any, Optional # pragma: no cover
class MockResponse: pass # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._headers_from_twisted_response = lambda response: {'Content-Type': 'application/json'} # pragma: no cover
result = { # pragma: no cover
    'txresponse': Mock(), # pragma: no cover
    'body': '{"key": "value"}', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '192.0.2.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
result['txresponse'].version = (1, 1, 1) # pragma: no cover
result['txresponse'].code = 200 # pragma: no cover
url = 'http://example.com' # pragma: no cover
def mock_from_args(headers: Dict[str, Any], url: str, body: str): # pragma: no cover
    return MockResponse() # pragma: no cover
responsetypes = type('MockResponseTypes', (object,), {'from_args': mock_from_args}) # pragma: no cover
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
