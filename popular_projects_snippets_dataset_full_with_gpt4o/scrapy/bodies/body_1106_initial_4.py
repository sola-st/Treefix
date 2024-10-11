from requests import Request, Response # pragma: no cover
from http.cookiejar import CookieJar # pragma: no cover

class WrappedRequest:# pragma: no cover
    def __init__(self, request):# pragma: no cover
        self.request = request # pragma: no cover
request = Request() # pragma: no cover
class WrappedResponse:# pragma: no cover
    def __init__(self, response):# pragma: no cover
        self.response = response # pragma: no cover
response = Response() # pragma: no cover
self = type('Mock', (object,), {'jar': CookieJar()}) # pragma: no cover

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
