from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers # pragma: no cover
from urllib.parse import urldefrag # pragma: no cover
from time import time # pragma: no cover

request = type('MockRequest', (object,), {'meta': {'download_timeout': 5}, 'url': 'http://example.com', 'method': 'GET', 'headers': {}})() # pragma: no cover
TxHeaders = Headers # pragma: no cover
request.body = None # pragma: no cover
timeout = request.meta.get('download_timeout') or self._connectTimeout # pragma: no cover
bodyproducer = None # pragma: no cover
def _cb_latency(latency, request, start_time): pass # pragma: no cover
def _cb_bodyready(response, request): pass # pragma: no cover
def _cb_bodydone(response, request, url): pass # pragma: no cover
def _cb_timeout(result, request, url, timeout): pass # pragma: no cover
reactor = type('MockReactor', (object,), {'callLater': lambda self, t, f: f(), 'stop': lambda self: None})() # pragma: no cover
d = type('Deferred', (object,), {'addCallback': lambda self, func, *args: func(0, *args), 'addBoth': lambda self, func, *args: func(0, *args), 'cancel': lambda self: None})() # pragma: no cover
exit = lambda x: None # pragma: no cover

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
