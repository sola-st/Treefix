from typing import Any, Dict # pragma: no cover
import types # pragma: no cover
import socket # pragma: no cover

self = type('Mock', (object,), {'_headers_from_twisted_response': lambda self, resp: {'Content-Type': 'text/html'}})() # pragma: no cover
result = {"txresponse": types.SimpleNamespace(version=(b'HTTP', 1, 1), code=200), "body": b'<html>Hello World</html>', "flags": [], "certificate": None, "ip_address": socket.gethostbyname(socket.gethostname()), "failure": None} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': lambda headers, url, body: type('ResponseClass', (object,), {})})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') if isinstance(x, bytes) else str(x) # pragma: no cover

from typing import Any, Dict # pragma: no cover
import types # pragma: no cover
import socket # pragma: no cover

self = type('Mock', (object,), {'_headers_from_twisted_response': lambda self, resp: {'Content-Type': 'text/html'}})() # pragma: no cover
result = {"txresponse": types.SimpleNamespace(version=(b'HTTP', 1, 1), code=200), "body": b'<html>Hello World</html>', "flags": [], "certificate": None, "ip_address": socket.gethostbyname(socket.gethostname()), "failure": None} # pragma: no cover
responsetypes = type('Mock', (object,), {'from_args': lambda **kwargs: type('ResponseClass', (object,), {})})() # pragma: no cover
url = 'http://example.com' # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') if isinstance(x, bytes) else str(x) # pragma: no cover

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
