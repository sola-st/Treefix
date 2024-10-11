from typing import Union # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
request = type('MockRequest', (object,), {'data': 'request_data'})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws) # pragma: no cover
signals = type('MockSignals', (object,), {'response_received': 'response_received'}) # pragma: no cover
self.slot = type('MockSlot', (object,), {'add_request': lambda x: None, 'nextcall': type('MockNextCall', (object,), {'schedule': lambda: None})()})() # pragma: no cover
self.spider = 'mock_spider' # pragma: no cover
self.logformatter = type('MockLogFormatter', (object,), {'crawled': lambda req, res, sp: {'message': 'crawled'}})() # pragma: no cover
self.signals = type('MockSignalsClass', (object,), {'send_catch_log': lambda **kwargs: None})() # pragma: no cover
self.downloader = type('MockDownloader', (object,), {'fetch': lambda req, sp: type('MockDeferred', (object,), {'addCallbacks': lambda func: None, 'addBoth': lambda func: None})()})() # pragma: no cover

from typing import Union # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
import logging # pragma: no cover
from scrapy import signals # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
spider = type('MockSpider', (object,), {'name': 'example_spider'})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws) # pragma: no cover
self.slot = type('MockSlot', (object,), {# pragma: no cover
 # pragma: no cover
'add_request': lambda req: None, # pragma: no cover
 # pragma: no cover
'nextcall': type('MockNextCall', (object,), {'schedule': lambda: None})() # pragma: no cover
 # pragma: no cover
})() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = type('MockLogFormatter', (object,), {'crawled': lambda req, res, spdr: {}})() # pragma: no cover
self.signals = type('MockSignalManager', (object,), {'send_catch_log': lambda signal, response, request, spider: None})() # pragma: no cover
self.downloader = type('MockDownloader', (object,), {'fetch': lambda req, spdr: type('MockDeferred', (object,), {'addCallbacks': lambda cb: None, 'addBoth': lambda cb: None})()})() # pragma: no cover
signals.response_received = object() # pragma: no cover

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
