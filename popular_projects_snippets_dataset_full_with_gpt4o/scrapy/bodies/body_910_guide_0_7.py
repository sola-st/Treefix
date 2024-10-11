from scrapy.http import Headers, Response # pragma: no cover
from twisted.web.http_headers import Headers as TwistedHeaders # pragma: no cover
from scrapy.utils.python import to_unicode # pragma: no cover
from scrapy.responsetypes import responsetypes # pragma: no cover

class MockTxResponse: # pragma: no cover
    version = ('HTTP', 1, 1) # pragma: no cover
    code = 200 # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
mock_txresponse = MockTxResponse() # pragma: no cover
url = 'http://example.com' # pragma: no cover
result = { # pragma: no cover
    'txresponse': mock_txresponse, # pragma: no cover
    'body': b'Hello, World!', # pragma: no cover
    'flags': [], # pragma: no cover
    'certificate': None, # pragma: no cover
    'ip_address': '127.0.0.1' # pragma: no cover
} # pragma: no cover
def _headers_from_twisted_response(txresponse): # pragma: no cover
    return Headers({'Content-Type': ['text/html']}) # pragma: no cover
self = type('MockSelf', (object,), {'_headers_from_twisted_response': _headers_from_twisted_response})() # pragma: no cover

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
