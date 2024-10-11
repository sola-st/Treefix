from typing import Any, Dict, Optional # pragma: no cover
import json # pragma: no cover
class MockResponse: ... # pragma: no cover
def to_unicode(value): return str(value) # pragma: no cover

class MockResponse: ... # pragma: no cover
def to_unicode(value): return str(value) # pragma: no cover
result = {"txresponse": {"version": [1, 1, 0], "code": 200}, "body": "response body", "flags": {}, "certificate": None, "ip_address": "192.168.1.1", "failure": None} # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda value: str(value) # pragma: no cover

from typing import Any, Dict, Optional # pragma: no cover
import json # pragma: no cover

class MockResponse: pass # pragma: no cover
class Mock:  # pragma: no cover
    def _headers_from_twisted_response(self, response): # pragma: no cover
        return {'Content-Type': 'application/json'} # pragma: no cover
self = Mock() # pragma: no cover
result = { # pragma: no cover
    'txresponse': {'version': [1, 1, 1], 'code': 200}, # pragma: no cover
    'body': json.dumps({'key': 'value'}), # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '192.0.2.1', # pragma: no cover
    'failure': None # pragma: no cover
} # pragma: no cover
url = 'http://example.com' # pragma: no cover
class MockResponseType:  # pragma: no cover
    def __init__(self, url, status, headers, body, flags, certificate, ip_address, protocol): # pragma: no cover
        self.url = url # pragma: no cover
        self.status = status # pragma: no cover
        self.headers = headers # pragma: no cover
        self.body = body # pragma: no cover
        self.flags = flags # pragma: no cover
        self.certificate = certificate # pragma: no cover
        self.ip_address = ip_address # pragma: no cover
        self.protocol = protocol # pragma: no cover
responsetypes = type('MockResponseTypes', (object,), {'from_args': staticmethod(lambda *args, **kwargs: MockResponseType(*args, **kwargs))})() # pragma: no cover
def to_unicode(value): return str(value) # pragma: no cover

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
