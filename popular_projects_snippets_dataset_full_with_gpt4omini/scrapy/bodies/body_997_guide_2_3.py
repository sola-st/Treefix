from typing import Union # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover
import logging # pragma: no cover

class MockSlot(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.nextcall = MockNextCall() # pragma: no cover
    def add_request(self, request): # pragma: no cover
        pass # pragma: no cover
class MockNextCall(object): # pragma: no cover
    def schedule(self): # pragma: no cover
        pass # pragma: no cover
class MockLogFormatter(object): # pragma: no cover
    def crawled(self, request, response, spider): # pragma: no cover
        return {'url': request.url, 'status': response.status} # pragma: no cover
class MockSignals(object): # pragma: no cover
    def send_catch_log(self, signal, response, request, spider): # pragma: no cover
        print(f'Sent Signal: {signal}, Response: {response}, Request: {request}, Spider: {spider}') # pragma: no cover
self = type('Mock', (object,), {'slot': MockSlot(), 'spider': 'mock_spider', 'logformatter': MockLogFormatter(), 'signals': MockSignals()})() # pragma: no cover
request = Request(url='http://example.com', method='GET') # pragma: no cover
self.downloader = type('MockDownloader', (object,), {'fetch': lambda self, req, spi: MockDeferred()})() # pragma: no cover
class MockDeferred(object): # pragma: no cover
    def addCallbacks(self, on_success): # pragma: no cover
        on_success(Response(url='http://example.com', status=200, request=req)) # pragma: no cover
    def addBoth(self, on_complete): # pragma: no cover
        on_complete(None) # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
assert self.slot is not None  # typing
_l_(8511)  # typing

self.slot.add_request(request)
_l_(8512)

if spider is None:
    _l_(8514)

    spider = self.spider
    _l_(8513)

def _on_success(result: Union[Response, Request]) -> Union[Response, Request]:
    _l_(8525)

    if not isinstance(result, (Response, Request)):
        _l_(8516)

        raise TypeError(f"Incorrect type: expected Response or Request, got {type(result)}: {result!r}")
        _l_(8515)
    if isinstance(result, Response):
        _l_(8523)

        if result.request is None:
            _l_(8518)

            result.request = request
            _l_(8517)
        logkws = self.logformatter.crawled(result.request, result, spider)
        _l_(8519)
        if logkws is not None:
            _l_(8521)

            logger.log(*logformatter_adapter(logkws), extra={"spider": spider})
            _l_(8520)
        self.signals.send_catch_log(
            signal=signals.response_received,
            response=result,
            request=result.request,
            spider=spider,
        )
        _l_(8522)
    aux = result
    _l_(8524)
    exit(aux)

def _on_complete(_):
    _l_(8528)

    self.slot.nextcall.schedule()
    _l_(8526)
    aux = _
    _l_(8527)
    exit(aux)

dwld = self.downloader.fetch(request, spider)
_l_(8529)
dwld.addCallbacks(_on_success)
_l_(8530)
dwld.addBoth(_on_complete)
_l_(8531)
aux = dwld
_l_(8532)
exit(aux)
