from twisted.web.http import Headers as TxHeaders # pragma: no cover
from twisted.web.client import Agent as TunnelingAgent # pragma: no cover
from twisted.web.client import HTTPConnectionPool # pragma: no cover
from twisted.internet import reactor, defer # pragma: no cover
from urllib.parse import urlparse, urlunparse, parse_qs # pragma: no cover
from time import time # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.meta = {'download_timeout': 30}# pragma: no cover
        self.url = 'http://example.com'# pragma: no cover
        self.method = 'GET'# pragma: no cover
        self.headers = {'User-Agent': 'test-agent'}# pragma: no cover
        self.body = None# pragma: no cover
request = MockRequest() # pragma: no cover
class Mock:# pragma: no cover
    _connectTimeout = 60# pragma: no cover
    def _get_agent(self, request, timeout): return TunnelingAgent(HTTPConnectionPool())# pragma: no cover
def urldefrag(url): return url, None # pragma: no cover
def to_bytes(string, encoding='utf-8'): return string.encode(encoding) # pragma: no cover
class MockHeaders:# pragma: no cover
    def __init__(self, headers):# pragma: no cover
        self.headers = headers# pragma: no cover
    def removeHeader(self, header):# pragma: no cover
        if header in self.headers:# pragma: no cover
            del self.headers[header]# pragma: no cover
TxHeaders = MockHeaders # pragma: no cover
class MockRequestBodyProducer:# pragma: no cover
    def __init__(self, body): pass# pragma: no cover
_RequestBodyProducer = MockRequestBodyProducer # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.web.client import Agent as TunnelingAgent # pragma: no cover
from twisted.web.client import HTTPConnectionPool # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from time import time # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.meta = {'download_timeout': 30}# pragma: no cover
        self.url = 'http://example.com'# pragma: no cover
        self.method = 'GET'# pragma: no cover
        self.headers = {'User-Agent': 'test-agent'}# pragma: no cover
        self.body = None# pragma: no cover
request = MockRequest() # pragma: no cover
class Mock:# pragma: no cover
    _connectTimeout = 60# pragma: no cover
    def _get_agent(self, request, timeout):# pragma: no cover
        return TunnelingAgent(HTTPConnectionPool(reactor))# pragma: no cover
    _TunnelingAgent = TunnelingAgent(HTTPConnectionPool(reactor))# pragma: no cover
self = Mock() # pragma: no cover
def urldefrag(url): return url, None # pragma: no cover
def to_bytes(string, encoding='utf-8'): return string.encode(encoding) # pragma: no cover
class MockHeaders:# pragma: no cover
    def __init__(self, headers):# pragma: no cover
        pass
# pragma: no cover
    def removeHeader(self, header):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
TxHeaders = MockHeaders(request.headers) # pragma: no cover
class MockRequestBodyProducer:# pragma: no cover
    def __init__(self, body): pass# pragma: no cover
_RequestBodyProducer = MockRequestBodyProducer # pragma: no cover

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
