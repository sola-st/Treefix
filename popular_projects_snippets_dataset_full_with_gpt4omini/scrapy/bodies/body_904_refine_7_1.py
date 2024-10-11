from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from urllib.parse import urlsplit, parse_qs # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.meta = {'download_timeout': 10}# pragma: no cover
        self.url = 'http://example.com'# pragma: no cover
        self.method = 'GET'# pragma: no cover
        self.headers = {'User-Agent': 'TestAgent'}# pragma: no cover
        self.body = None# pragma: no cover
# pragma: no cover
request = MockRequest() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._connectTimeout = 15# pragma: no cover
        self._TunnelingAgent = Agent# pragma: no cover
        self._cb_latency = lambda *args: None# pragma: no cover
        self._cb_bodyready = lambda *args: None# pragma: no cover
        self._cb_bodydone = lambda *args: None# pragma: no cover
        self._timeout_cl = None# pragma: no cover
        self._cb_timeout = lambda *args: None# pragma: no cover
# pragma: no cover
    def _get_agent(self, request, timeout):# pragma: no cover
        return Agent(reactor)# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
def urldefrag(url):# pragma: no cover
    return (url, '')# pragma: no cover
 # pragma: no cover
def to_bytes(value, encoding='utf-8'):# pragma: no cover
    return value.encode(encoding)# pragma: no cover
 # pragma: no cover
def _RequestBodyProducer(body):# pragma: no cover
    class MockBodyProducer:# pragma: no cover
        def __init__(self, body):# pragma: no cover
            self.body = body# pragma: no cover
    return MockBodyProducer(body)# pragma: no cover
 # pragma: no cover
 # pragma: no cover

from twisted.web.client import Agent # pragma: no cover
from twisted.web.http_headers import Headers as TxHeaders # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from time import time # pragma: no cover
from urllib.parse import urlsplit, parse_qs # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.meta = {'download_timeout': 10}# pragma: no cover
        self.url = 'http://example.com'# pragma: no cover
        self.method = 'GET'# pragma: no cover
        self.headers = {'User-Agent': 'TestAgent'}# pragma: no cover
        self.body = None# pragma: no cover
# pragma: no cover
request = MockRequest() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._connectTimeout = 15# pragma: no cover
        self._TunnelingAgent = Agent# pragma: no cover
        self._cb_latency = lambda *args: None# pragma: no cover
        self._cb_bodyready = lambda *args: None# pragma: no cover
        self._cb_bodydone = lambda *args: None# pragma: no cover
        self._timeout_cl = None# pragma: no cover
        self._cb_timeout = lambda *args: None# pragma: no cover
# pragma: no cover
    def _get_agent(self, request, timeout):# pragma: no cover
        return Agent(reactor)# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
def urldefrag(url):# pragma: no cover
    return (url, '')# pragma: no cover
 # pragma: no cover
def to_bytes(value, encoding='utf-8'):# pragma: no cover
    return value.encode(encoding)# pragma: no cover
 # pragma: no cover
class _RequestBodyProducer:# pragma: no cover
    def __init__(self, body):# pragma: no cover
        self.body = body# pragma: no cover
# pragma: no cover
_RequestBodyProducer = _RequestBodyProducer # pragma: no cover
time = time # pragma: no cover

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
