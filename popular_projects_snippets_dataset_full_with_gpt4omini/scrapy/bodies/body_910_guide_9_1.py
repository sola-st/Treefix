from typing import Dict, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

result: Dict[str, Any] = { # pragma: no cover
    'txresponse': Mock(version=(1, 1, 1), code=200), # pragma: no cover
    'body': b'mock response body', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '192.0.2.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = str # pragma: no cover
class MockResponse: # pragma: no cover
    def __init__(self, url, status, headers, body, flags, certificate, ip_address, protocol): # pragma: no cover
        self.url = url # pragma: no cover
        self.status = status # pragma: no cover
        self.headers = headers # pragma: no cover
        self.body = body # pragma: no cover
        self.flags = flags # pragma: no cover
        self.certificate = certificate # pragma: no cover
        self.ip_address = ip_address # pragma: no cover
        self.protocol = protocol # pragma: no cover
responsetypes = Mock() # pragma: no cover
responsetypes.from_args = Mock(return_value=MockResponse(url, int(result['txresponse'].code), {}, result['body'], result['flags'], result['certificate'], result['ip_address'], None)) # pragma: no cover
self = Mock() # pragma: no cover
self._headers_from_twisted_response = Mock(return_value={'Content-Type': 'application/json'}) # pragma: no cover

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
