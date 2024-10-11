from twisted.internet import reactor # pragma: no cover
from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from urllib.parse import urldefrag # pragma: no cover
from time import time # pragma: no cover

class MockRequest: pass # pragma: no cover
request = MockRequest() # pragma: no cover
request.meta = {'download_timeout': 10} # pragma: no cover
request.url = 'http://example.com/resource' # pragma: no cover
request.method = 'GET' # pragma: no cover
request.headers = {'User-Agent': 'test-agent'} # pragma: no cover
request.body = b'Some body content' # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._connectTimeout = 5 # pragma: no cover
self._get_agent = lambda req, timeout: Agent(reactor) # pragma: no cover
self._TunnelingAgent = None # pragma: no cover
timeout = request.meta.get('download_timeout') or self._connectTimeout # pragma: no cover
agent = self._get_agent(request, timeout) # pragma: no cover
url = urldefrag(request.url)[0] # pragma: no cover
to_bytes = lambda s, encoding='utf-8': s.encode(encoding) if isinstance(s, str) else s # pragma: no cover
headers = TxHeaders(request.headers) # pragma: no cover
class _RequestBodyProducer: pass # pragma: no cover
bodyproducer = _RequestBodyProducer() if request.body else None # pragma: no cover
start_time = time() # pragma: no cover
d = agent.request(to_bytes(request.method), to_bytes(url, encoding='ascii'), headers, bodyproducer) # pragma: no cover
self._cb_latency = lambda d, req, start: None # pragma: no cover
self._cb_bodyready = lambda d, req: None # pragma: no cover
self._cb_bodydone = lambda d, req, url: None # pragma: no cover
self._cb_timeout = lambda d, req, url, timeout: None # pragma: no cover
self._timeout_cl = reactor.callLater(timeout, d.cancel) # pragma: no cover
d.addCallback(self._cb_latency, request, start_time) # pragma: no cover
d.addCallback(self._cb_bodyready, request) # pragma: no cover
d.addCallback(self._cb_bodydone, request, url) # pragma: no cover
d.addBoth(self._cb_timeout, request, url, timeout) # pragma: no cover
aux = d # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
try:
    from twisted.internet import reactor
    _l_(7976)

except ImportError:
    pass
timeout = request.meta.get('download_timeout') or self._connectTimeout
_l_(7977)
agent = self._get_agent(request, timeout)
_l_(7978)

# request details
url = urldefrag(request.url)[0]
_l_(7979)
method = to_bytes(request.method)
_l_(7980)
headers = TxHeaders(request.headers)
_l_(7981)
if isinstance(agent, self._TunnelingAgent):
    _l_(7983)

    headers.removeHeader(b'Proxy-Authorization')
    _l_(7982)
if request.body:
    _l_(7986)

    bodyproducer = _RequestBodyProducer(request.body)
    _l_(7984)
else:
    bodyproducer = None
    _l_(7985)
start_time = time()
_l_(7987)
d = agent.request(method, to_bytes(url, encoding='ascii'), headers, bodyproducer)
_l_(7988)
# set download latency
d.addCallback(self._cb_latency, request, start_time)
_l_(7989)
# response body is ready to be consumed
d.addCallback(self._cb_bodyready, request)
_l_(7990)
d.addCallback(self._cb_bodydone, request, url)
_l_(7991)
# check download timeout
self._timeout_cl = reactor.callLater(timeout, d.cancel)
_l_(7992)
d.addBoth(self._cb_timeout, request, url, timeout)
_l_(7993)
aux = d
_l_(7994)
exit(aux)
