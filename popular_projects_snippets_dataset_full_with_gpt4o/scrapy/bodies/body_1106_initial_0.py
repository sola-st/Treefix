from http.server import BaseHTTPRequestHandler, HTTPServer # pragma: no cover
import types # pragma: no cover

response = type('Response', (object,), {'read': lambda self: b''})() # pragma: no cover
WrappedRequest = lambda req: req # pragma: no cover
WrappedResponse = lambda res: res # pragma: no cover
self = type('Self', (object,), {'jar': type('MockJar', (object,), {'extract_cookies': lambda self, wrsp, wreq: None})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
wreq = WrappedRequest(request)
_l_(18744)
wrsp = WrappedResponse(response)
_l_(18745)
aux = self.jar.extract_cookies(wrsp, wreq)
_l_(18746)
exit(aux)
