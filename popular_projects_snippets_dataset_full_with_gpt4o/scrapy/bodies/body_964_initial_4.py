from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import reactor # pragma: no cover

mustbe_deferred = lambda fn, *args, **kwargs: Deferred().addCallback(lambda _: fn(*args, **kwargs)) # pragma: no cover
class MockSignals: # pragma: no cover
    def send_catch_log(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
signals = type('signals', (object,), { # pragma: no cover
    'response_downloaded': 'response_downloaded_signal', # pragma: no cover
    'request_left_downloader': 'request_left_downloader_signal' # pragma: no cover
}) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'handlers': type('Handlers', (object,), { # pragma: no cover
        'download_request': lambda request, spider: 'downloaded_content' # pragma: no cover
    })(), # pragma: no cover
    'signals': MockSignals(), # pragma: no cover
    '_process_queue': lambda self, spider, slot: None # pragma: no cover
})() # pragma: no cover
request = type('Request', (object,), {})() # pragma: no cover
spider = type('Spider', (object,), {})() # pragma: no cover
slot = type('Slot', (object,), { # pragma: no cover
    'transferring': set() # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
# The order is very important for the following deferreds. Do not change!

# 1. Create the download deferred
from l3.Runtime import _l_
dfd = mustbe_deferred(self.handlers.download_request, request, spider)
_l_(21528)

# 2. Notify response_downloaded listeners about the recent download
# before querying queue for next request
def _downloaded(response):
    _l_(21531)

    self.signals.send_catch_log(signal=signals.response_downloaded,
                                response=response,
                                request=request,
                                spider=spider)
    _l_(21529)
    aux = response
    _l_(21530)
    exit(aux)
dfd.addCallback(_downloaded)
_l_(21532)

# 3. After response arrives, remove the request from transferring
# state to free up the transferring slot so it can be used by the
# following requests (perhaps those which came from the downloader
# middleware itself)
slot.transferring.add(request)
_l_(21533)

def finish_transferring(_):
    _l_(21538)

    slot.transferring.remove(request)
    _l_(21534)
    self._process_queue(spider, slot)
    _l_(21535)
    self.signals.send_catch_log(signal=signals.request_left_downloader,
                                request=request,
                                spider=spider)
    _l_(21536)
    aux = _
    _l_(21537)
    exit(aux)
aux = dfd.addBoth(finish_transferring)
_l_(21539)

exit(aux)
