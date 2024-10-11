from http.cookies import SimpleCookie # pragma: no cover
from typing import Any # pragma: no cover

class WrappedRequest:# pragma: no cover
    def __init__(self, request):# pragma: no cover
        self.request = request # pragma: no cover
request = {'method': 'GET', 'url': 'http://example.com'} # pragma: no cover
class WrappedResponse:# pragma: no cover
    def __init__(self, response):# pragma: no cover
        self.response = response # pragma: no cover
response = {'status_code': 200, 'headers': {}} # pragma: no cover
class MockJar:# pragma: no cover
    def extract_cookies(self, response, request):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {'jar': MockJar()})() # pragma: no cover

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
