from typing import Union # pragma: no cover
class Response: pass # pragma: no cover
class Request: pass # pragma: no cover
import logging # pragma: no cover
import types # pragma: no cover
from twisted.internet import defer # pragma: no cover

self = type('MockSelf', (object,), {# pragma: no cover
 # pragma: no cover
'slot': type('MockSlot', (object,), {'add_request': lambda self, request: None, 'nextcall': type('MockNextCall', (object,), {'schedule': lambda self: None})()})(), # pragma: no cover
 # pragma: no cover
'spider': type('MockSpider', (object,), {})(), # pragma: no cover
 # pragma: no cover
'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda self, request, result, spider: {}})(), # pragma: no cover
 # pragma: no cover
'signals': type('MockSignals', (object,), {'send_catch_log': lambda self, signal, response, request, spider: None})(), # pragma: no cover
 # pragma: no cover
'downloader': type('MockDownloader', (object,), {'fetch': lambda self, request, spider: defer.Deferred()})()# pragma: no cover
 # pragma: no cover
})() # pragma: no cover
request = Request() # pragma: no cover
spider = None # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, 'message') # pragma: no cover
signals = type('MockSignalsModule', (object,), {'response_received': object()})() # pragma: no cover

from typing import Union # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover
import logging # pragma: no cover
class Response: pass # pragma: no cover
class Request: pass # pragma: no cover

self = type('MockSelf', (object,), {# pragma: no cover
 # pragma: no cover
'slot': type('MockSlot', (object,), {'add_request': lambda self, request: None, 'nextcall': type('MockNextCall', (object,), {'schedule': lambda self: None})()})(), # pragma: no cover
 # pragma: no cover
'spider': type('MockSpider', (object,), {})(), # pragma: no cover
 # pragma: no cover
'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda self, request, result, spider: {}})(), # pragma: no cover
 # pragma: no cover
'signals': type('MockSignals', (object,), {'send_catch_log': lambda self, signal, response, request, spider: None})(), # pragma: no cover
 # pragma: no cover
'downloader': type('MockDownloader', (object,), {'fetch': lambda self, request, spider: Deferred()})()# pragma: no cover
 # pragma: no cover
})() # pragma: no cover
request = Request() # pragma: no cover
spider = None # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, 'message') # pragma: no cover
signals = type('MockSignalsModule', (object,), {'response_received': object()})() # pragma: no cover

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
