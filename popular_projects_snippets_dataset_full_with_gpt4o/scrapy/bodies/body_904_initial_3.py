from urllib.parse import urldefrag # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from twisted.internet import reactor # pragma: no cover
import time # pragma: no cover

request = type('Request', (object,), {'meta': {'download_timeout': 30}, 'url': 'http://example.com', 'method': 'GET', 'headers': {}, 'body': b'test'})() # pragma: no cover
self = type('MockSelf', (object,), {'_connectTimeout': 20, '_get_agent': lambda self, req, timeout: type('MockAgent', (object,), {'request': lambda self, method, url, headers, body: None})(), '_TunnelingAgent': type('MockTunnelingAgent', (object,), {})})() # pragma: no cover
to_bytes = lambda s, encoding='utf-8': s.encode(encoding) if isinstance(s, str) else s # pragma: no cover
_RequestBodyProducer = lambda body: type('MockBodyProducer', (object,), {'body': body})() # pragma: no cover
time = time.time # pragma: no cover
MockAgent = type('MockAgent', (object,), {'request': lambda self, method, url, headers, body: None}) # pragma: no cover
self._cb_latency = lambda response, request, start: None # pragma: no cover
self._cb_bodyready = lambda response, request: None # pragma: no cover
self._cb_bodydone = lambda response, request, url: None # pragma: no cover
self._cb_timeout = lambda response, request, url, timeout: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
try:
    from twisted.internet import reactor
    _l_(18708)

except ImportError:
    pass
timeout = request.meta.get('download_timeout') or self._connectTimeout
_l_(18709)
agent = self._get_agent(request, timeout)
_l_(18710)

# request details
url = urldefrag(request.url)[0]
_l_(18711)
method = to_bytes(request.method)
_l_(18712)
headers = TxHeaders(request.headers)
_l_(18713)
if isinstance(agent, self._TunnelingAgent):
    _l_(18715)

    headers.removeHeader(b'Proxy-Authorization')
    _l_(18714)
if request.body:
    _l_(18718)

    bodyproducer = _RequestBodyProducer(request.body)
    _l_(18716)
else:
    bodyproducer = None
    _l_(18717)
start_time = time()
_l_(18719)
d = agent.request(method, to_bytes(url, encoding='ascii'), headers, bodyproducer)
_l_(18720)
# set download latency
d.addCallback(self._cb_latency, request, start_time)
_l_(18721)
# response body is ready to be consumed
d.addCallback(self._cb_bodyready, request)
_l_(18722)
d.addCallback(self._cb_bodydone, request, url)
_l_(18723)
# check download timeout
self._timeout_cl = reactor.callLater(timeout, d.cancel)
_l_(18724)
d.addBoth(self._cb_timeout, request, url, timeout)
_l_(18725)
aux = d
_l_(18726)
exit(aux)
