from typing import Any, Dict # pragma: no cover
class MockResponse: pass # pragma: no cover
def to_unicode(value): return str(value) # pragma: no cover

self = type('Mock', (), {'_headers_from_twisted_response': lambda x: {'Content-Type': 'application/json'}})() # pragma: no cover
result = { 'txresponse': type('MockResponse', (), {'version': ['HTTP', 1, 1], 'code': '200'})(), 'body': '{}', 'flags': [], 'certificate': None, 'ip_address': '127.0.0.1', 'failure': None } # pragma: no cover

from typing import Any, Dict # pragma: no cover

class Self:# pragma: no cover
    def _headers_from_twisted_response(self, response):# pragma: no cover
        return {'Content-Type': 'application/json'}# pragma: no cover
# pragma: no cover
self = Self() # pragma: no cover
result = {"txresponse": {"version": [1, 1, 1], "code": 200}, "body": 'Response Body', "flags": {}, "certificate": None, "ip_address": '192.168.1.1', "failure": None} # pragma: no cover
class MockResponseTypes:# pragma: no cover
    @staticmethod# pragma: no cover
    def from_args(headers, url, body):# pragma: no cover
        return lambda url, status, headers, body, flags, certificate, ip_address, protocol: {'url': url, 'status': status, 'headers': headers, 'body': body, 'flags': flags, 'certificate': certificate, 'ip_address': ip_address, 'protocol': protocol}# pragma: no cover
# pragma: no cover
responsetypes = MockResponseTypes # pragma: no cover
url = 'http://example.com' # pragma: no cover
def to_unicode(value):# pragma: no cover
    return str(value) # pragma: no cover

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
