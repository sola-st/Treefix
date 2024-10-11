from typing import Union # pragma: no cover
import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self.slot = Mock() # pragma: no cover
self.slot.add_request = Mock() # pragma: no cover
request = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
self.spider = Mock() # pragma: no cover
class Response: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.request = None # pragma: no cover
class Request: # pragma: no cover
    pass # pragma: no cover
Union = Union # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = Mock() # pragma: no cover
self.logformatter = Mock() # pragma: no cover
self.logformatter.crawled = Mock() # pragma: no cover
self.signals = Mock() # pragma: no cover
self.downloader = Mock() # pragma: no cover
self.downloader.fetch = Mock(return_value=Mock()) # pragma: no cover

from typing import Union # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
import logging # pragma: no cover
from twisted.internet import defer # pragma: no cover
from scrapy import signals # pragma: no cover

request = Request(url='http://example.com') # pragma: no cover
spider = type('MockSpider', (object,), {'name': 'example_spider'})() # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws) # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.slot = type('MockSlot', (object,), {'add_request': lambda req: None, 'nextcall': type('MockNextCall', (object,), {'schedule': lambda: None})()})() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = type('MockLogFormatter', (object,), {'crawled': lambda req, res, spdr: {'level': logging.INFO, 'msg': 'Crawled'}})() # pragma: no cover
self.signals = type('MockSignalManager', (object,), {'send_catch_log': lambda signal, response, request, spider: None})() # pragma: no cover
self.downloader = type('MockDownloader', (object,), {'fetch': lambda req, spdr: defer.Deferred()})() # pragma: no cover
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
