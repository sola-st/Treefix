from typing import Union # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover
import logging # pragma: no cover

class Request: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Response: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.request = None # pragma: no cover
 # pragma: no cover
class Logger: # pragma: no cover
    def log(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def logformatter_adapter(logkws): # pragma: no cover
    return (loggin.INFO, logkws) # pragma: no cover
 # pragma: no cover
class LogFormatter: # pragma: no cover
    def crawled(self, request, response, spider): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
class Signals: # pragma: no cover
    def send_catch_log(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class Slot: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.nextcall = self # pragma: no cover
    def schedule(self): # pragma: no cover
        pass # pragma: no cover
    def add_request(self, request): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class Downloader: # pragma: no cover
    def fetch(self, request, spider): # pragma: no cover
        d = Deferred() # pragma: no cover
        d.callback(Response()) # pragma: no cover
        return d # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'slot': Slot(), # pragma: no cover
    'spider': 'dummy_spider', # pragma: no cover
    'logformatter': LogFormatter(), # pragma: no cover
    'signals': Signals(), # pragma: no cover
    'downloader': Downloader() # pragma: no cover
})() # pragma: no cover
request = Request() # pragma: no cover
spider = None # pragma: no cover
logger = Logger() # pragma: no cover

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
