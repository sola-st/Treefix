from scrapy import signals # pragma: no cover

self = type('MockSelf', (object,), {'handlers': type('MockHandlers', (object,), {'download_request': lambda req, spi: 'downloaded'})(), 'signals': type('MockSignals', (object,), {'send_catch_log': lambda signal, response, request, spider: None})()})() # pragma: no cover
request = 'mock_request' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
slot = type('MockSlot', (object,), {'transferring': set()})() # pragma: no cover
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
