from requests.cookies import RequestsCookieJar # pragma: no cover
from requests.models import Request # pragma: no cover
from requests.models import Response # pragma: no cover

WrappedRequest = type('WrappedRequest', (object,), {}) # pragma: no cover
request = Request() # pragma: no cover
WrappedResponse = type('WrappedResponse', (object,), {}) # pragma: no cover
response = Response() # pragma: no cover
self = type('MockSelf', (object,), {'jar': RequestsCookieJar()})() # pragma: no cover

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
