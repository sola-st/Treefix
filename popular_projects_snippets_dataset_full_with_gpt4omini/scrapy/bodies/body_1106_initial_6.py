from http.cookies import SimpleCookie # pragma: no cover
from requests import Request, Response # pragma: no cover
from requests.cookies import RequestsCookieJar # pragma: no cover

class WrappedRequest(Request): pass # pragma: no cover
request = WrappedRequest('GET', 'http://example.com') # pragma: no cover
class WrappedResponse(Response): pass # pragma: no cover
response = WrappedResponse() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
from l3.Runtime import _l_
wreq = WrappedRequest(request)
_l_(7850)
wrsp = WrappedResponse(response)
_l_(7851)
aux = self.jar.extract_cookies(wrsp, wreq)
_l_(7852)
exit(aux)
