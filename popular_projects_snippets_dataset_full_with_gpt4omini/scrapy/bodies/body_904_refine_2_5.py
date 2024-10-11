from twisted.web.http import Request as TwistedRequest # pragma: no cover
from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from urllib.parse import urlparse, urlunparse # pragma: no cover
import time as time_module # pragma: no cover

self = type('Mock', (object,), { '_connectTimeout': 30, '_get_agent': lambda self, req, timeout: Agent(reactor), '_TunnelingAgent': Agent })() # pragma: no cover
urldefrag = lambda url: (urlparse(url).geturl(), '') # pragma: no cover
to_bytes = lambda s, encoding='utf-8': s.encode(encoding) # pragma: no cover
TxHeaders = lambda headers: Headers({k.encode('utf-8'): [v.encode('utf-8')] for k, v in headers.items()}) # pragma: no cover
_RequestBodyProducer = lambda body: body # pragma: no cover
time = time_module.time # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from urllib.parse import urlparse # pragma: no cover
import time as time_module # pragma: no cover

request = type('MockRequest', (), { 'url': 'http://example.com', 'method': 'GET', 'headers': { 'User-Agent': 'my-agent' }, 'body': None, 'meta': { 'download_timeout': 5 } })() # pragma: no cover
urldefrag = lambda url: (urlparse(url).geturl(), None) # pragma: no cover
to_bytes = lambda s, encoding='utf-8': s.encode(encoding) # pragma: no cover
TxHeaders = lambda headers: Headers({k.encode('utf-8'): [v.encode('utf-8')] for k, v in headers.items()}) # pragma: no cover
_RequestBodyProducer = lambda body: BodyProducer(body.encode('utf-8')) if body else None # pragma: no cover
time = time_module.time # pragma: no cover

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
