from http.cookies import SimpleCookie # pragma: no cover
from typing import Any # pragma: no cover

WrappedRequest = type('WrappedRequest', (object,), {}) # pragma: no cover
request = WrappedRequest() # pragma: no cover
WrappedResponse = type('WrappedResponse', (object,), {}) # pragma: no cover
response = WrappedResponse() # pragma: no cover
self = type('SelfType', (object,), {'jar': type('Mock', (object,), {'extract_cookies': lambda self, wrsp, wreq: None})()})() # pragma: no cover

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
