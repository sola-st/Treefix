from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.task import deferLater # pragma: no cover
from twisted.internet import reactor # pragma: no cover

mustbe_deferred = lambda func, *args: deferLater(reactor, 0, func, *args) # pragma: no cover
class Handlers: download_request = lambda req, spd: Deferred() # pragma: no cover

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
