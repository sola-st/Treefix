from http.cookies import SimpleCookie # pragma: no cover
from types import SimpleNamespace # pragma: no cover

WrappedRequest = SimpleNamespace # pragma: no cover
request = SimpleNamespace() # pragma: no cover
WrappedResponse = SimpleNamespace # pragma: no cover
response = SimpleNamespace() # pragma: no cover
self = SimpleNamespace(jar=SimpleNamespace(extract_cookies=lambda wrsp, wreq: None)) # pragma: no cover

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
