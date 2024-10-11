from scrapy import signals # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockHandlers: # pragma: no cover
    def download_request(self, request, spider): # pragma: no cover
        dfd = Deferred() # pragma: no cover
        dfd.callback('mock_response') # pragma: no cover
        return dfd # pragma: no cover
 # pragma: no cover
class MockSignals: # pragma: no cover
    def send_catch_log(self, signal, **kwargs): # pragma: no cover
        print(f'Log signal: {signal}, kwargs: {kwargs}') # pragma: no cover
 # pragma: no cover
class MockSlot: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.transferring = set() # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'handlers': MockHandlers(), # pragma: no cover
    'signals': MockSignals(), # pragma: no cover
    '_process_queue': lambda spider, slot: print('Processing queue...') # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
request = 'mock_request' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
slot = MockSlot() # pragma: no cover

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
