from http.cookies import SimpleCookie # pragma: no cover

WrappedRequest = type('WrappedRequest', (object,), {}) # pragma: no cover
request = type('MockRequest', (object,), {})() # pragma: no cover
WrappedResponse = type('WrappedResponse', (object,), {}) # pragma: no cover
response = type('MockResponse', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), {'jar': type('MockJar', (object,), {'extract_cookies': lambda self, wrsp, wreq: print('Extracting cookies')})()})() # pragma: no cover

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
