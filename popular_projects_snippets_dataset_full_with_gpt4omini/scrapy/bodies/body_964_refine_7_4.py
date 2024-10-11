from twisted.internet import defer # pragma: no cover
from scrapy import signals # pragma: no cover

mustbe_deferred = defer.Deferred # pragma: no cover
self = type('Mock', (), {'handlers': type('MockHandlers', (), {'download_request': lambda req, sp: defer.Deferred()})(), 'signals': type('MockSignals', (), {'send_catch_log': lambda signal, **kwargs: None})()})() # pragma: no cover
request = {'url': 'http://example.com', 'method': 'GET', 'body': None} # pragma: no cover
spider = type('MockSpider', (), {'name': 'example_spider'})() # pragma: no cover
slot = type('MockSlot', (), {'transferring': set()})() # pragma: no cover
signals = signals # pragma: no cover

from twisted.internet.defer import Deferred # pragma: no cover
from scrapy import signals # pragma: no cover

class MockHandlers: # pragma: no cover
    def download_request(self, request, spider): # pragma: no cover
        return 'downloaded_data' # pragma: no cover
class MockSignals: # pragma: no cover
    def send_catch_log(self, signal, **kwargs): # pragma: no cover
        pass # pragma: no cover
self = type('MockSelf', (), {'handlers': MockHandlers(), 'signals': MockSignals()})() # pragma: no cover
request = {'url': 'http://example.com', 'method': 'GET'} # pragma: no cover
spider = 'mock_spider' # pragma: no cover
slot = type('MockSlot', (), {'transferring': set()})() # pragma: no cover
def mustbe_deferred(handler, *args): return Deferred().addCallback(lambda _: handler(*args)) # pragma: no cover
signals = signals # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
# The order is very important for the following deferreds. Do not change!

# 1. Create the download deferred
from l3.Runtime import _l_
dfd = mustbe_deferred(self.handlers.download_request, request, spider)
_l_(10154)

# 2. Notify response_downloaded listeners about the recent download
# before querying queue for next request
def _downloaded(response):
    _l_(10157)

    self.signals.send_catch_log(signal=signals.response_downloaded,
                                response=response,
                                request=request,
                                spider=spider)
    _l_(10155)
    aux = response
    _l_(10156)
    exit(aux)
dfd.addCallback(_downloaded)
_l_(10158)

# 3. After response arrives, remove the request from transferring
# state to free up the transferring slot so it can be used by the
# following requests (perhaps those which came from the downloader
# middleware itself)
slot.transferring.add(request)
_l_(10159)

def finish_transferring(_):
    _l_(10164)

    slot.transferring.remove(request)
    _l_(10160)
    self._process_queue(spider, slot)
    _l_(10161)
    self.signals.send_catch_log(signal=signals.request_left_downloader,
                                request=request,
                                spider=spider)
    _l_(10162)
    aux = _
    _l_(10163)
    exit(aux)
aux = dfd.addBoth(finish_transferring)
_l_(10165)

exit(aux)
