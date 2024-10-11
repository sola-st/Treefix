from types import SimpleNamespace # pragma: no cover
class WrappedRequest: pass # pragma: no cover
class WrappedResponse: pass # pragma: no cover
class CookieJar: pass # pragma: no cover

request = SimpleNamespace(headers={}, cookies={}) # pragma: no cover
response = SimpleNamespace(headers={}, cookies={}) # pragma: no cover
self = SimpleNamespace(jar=CookieJar()) # pragma: no cover
self.jar.extract_cookies = lambda wrsp, wreq: None # pragma: no cover

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
