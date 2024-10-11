from typing import Union # pragma: no cover
import logging # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
spider = type('Mock', (object,), {})() # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws) # pragma: no cover
self.slot = type('Mock', (object,), {'add_request': lambda self, req: None, 'nextcall': type('Mock', (object,), {'schedule': lambda self: None})()})() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = type('Mock', (object,), {'crawled': lambda self, req, res, spdr: {'message': 'Crawled'}})() # pragma: no cover
self.signals = type('Mock', (object,), {'send_catch_log': lambda self, signal, response, request, spider: None})() # pragma: no cover
self.downloader = type('Mock', (object,), {'fetch': lambda self, req, spdr: type('Mock', (object,), {'addCallbacks': lambda self, callback: None, 'addBoth': lambda self, callback: None})()})() # pragma: no cover

from typing import Union # pragma: no cover
import logging # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockSlot: # pragma: no cover
    def add_request(self, request): # pragma: no cover
        pass # pragma: no cover
    class NextCall: # pragma: no cover
        def schedule(self): # pragma: no cover
            pass # pragma: no cover
    nextcall = NextCall() # pragma: no cover
class MockLogFormatter: # pragma: no cover
    def crawled(self, request, response, spider): # pragma: no cover
        return {'level': logging.INFO, 'msg': 'Crawled', 'args': ()} # pragma: no cover
class MockSignals: # pragma: no cover
    def send_catch_log(self, signal, response, request, spider): # pragma: no cover
        pass # pragma: no cover
class MockDownloader: # pragma: no cover
    def fetch(self, request, spider): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.addCallbacks(self._dummy_success) # pragma: no cover
        d.addBoth(self._dummy_complete) # pragma: no cover
        d.callback(Response(url='http://example.com')) # Immediately call the callback for testing purposes # pragma: no cover
        return d # pragma: no cover
    def _dummy_success(self, result): # pragma: no cover
        return result # pragma: no cover
    def _dummy_complete(self, result): # pragma: no cover
        return result # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
spider = None # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logformatter_adapter = lambda logkws: (logkws['level'], logkws['msg']) # pragma: no cover
self.slot = MockSlot() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = MockLogFormatter() # pragma: no cover
self.signals = MockSignals() # pragma: no cover
self.downloader = MockDownloader() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
assert self.slot is not None  # typing
_l_(18759)  # typing

self.slot.add_request(request)
_l_(18760)

if spider is None:
    _l_(18762)

    spider = self.spider
    _l_(18761)

def _on_success(result: Union[Response, Request]) -> Union[Response, Request]:
    _l_(18773)

    if not isinstance(result, (Response, Request)):
        _l_(18764)

        raise TypeError(f"Incorrect type: expected Response or Request, got {type(result)}: {result!r}")
        _l_(18763)
    if isinstance(result, Response):
        _l_(18771)

        if result.request is None:
            _l_(18766)

            result.request = request
            _l_(18765)
        logkws = self.logformatter.crawled(result.request, result, spider)
        _l_(18767)
        if logkws is not None:
            _l_(18769)

            logger.log(*logformatter_adapter(logkws), extra={"spider": spider})
            _l_(18768)
        self.signals.send_catch_log(
            signal=signals.response_received,
            response=result,
            request=result.request,
            spider=spider,
        )
        _l_(18770)
    aux = result
    _l_(18772)
    exit(aux)

def _on_complete(_):
    _l_(18776)

    self.slot.nextcall.schedule()
    _l_(18774)
    aux = _
    _l_(18775)
    exit(aux)

dwld = self.downloader.fetch(request, spider)
_l_(18777)
dwld.addCallbacks(_on_success)
_l_(18778)
dwld.addBoth(_on_complete)
_l_(18779)
aux = dwld
_l_(18780)
exit(aux)
