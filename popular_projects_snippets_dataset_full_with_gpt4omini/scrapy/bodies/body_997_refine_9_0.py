from typing import Union # pragma: no cover
from scrapy.http import Request, Response # pragma: no cover
import logging # pragma: no cover
from scrapy import signals # pragma: no cover
from twisted.internet import defer # pragma: no cover

class MockSlot:  # represents self.slot# pragma: no cover
    def add_request(self, request): pass# pragma: no cover
    def nextcall(self): return self# pragma: no cover
    def schedule(self): pass# pragma: no cover
request = Request(url='http://example.com', method='GET') # pragma: no cover
spider = 'example_spider' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
def logformatter_adapter(logkws): return (logkws['status'], logkws['url']) # pragma: no cover
class MockLogFormatter:# pragma: no cover
    def crawled(self, request, response, spider):# pragma: no cover
        return {'status': 200, 'url': request.url}# pragma: no cover
class MockDownloader:# pragma: no cover
    def fetch(self, request, spider):# pragma: no cover
        return defer.Deferred()  # mock deferred object# pragma: no cover
class MockSignals:# pragma: no cover
    def send_catch_log(self, signal, response, request, spider): pass# pragma: no cover
signals.response_received = 'response_received_signal' # pragma: no cover

from typing import Union # pragma: no cover
from scrapy.http import Request, Response # pragma: no cover
import logging # pragma: no cover
from scrapy import signals # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockSlot:  # represents self.slot# pragma: no cover
    def add_request(self, request): pass# pragma: no cover
    def nextcall(self): return self# pragma: no cover
    def schedule(self): pass # pragma: no cover
class MockLogFormatter:  # represents self.logformatter# pragma: no cover
    def crawled(self, request, response, spider):# pragma: no cover
        return {'msg': 'crawled', 'request': request, 'response': response}# pragma: no cover
class MockDownloader:  # represents self.downloader# pragma: no cover
    def fetch(self, request, spider):# pragma: no cover
        return Deferred()  # return a mock Deferred object# pragma: no cover
class MockSignals:  # represents self.signals# pragma: no cover
    response_received = 'response_received'# pragma: no cover
    def send_catch_log(self, signal, response, request, spider): pass# pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
spider = 'example_spider'  # Placeholder for the spider's name # pragma: no cover
logger = logging.getLogger('example_logger')# pragma: no cover
logger.setLevel(logging.INFO)  # Setting the logging level # pragma: no cover
logformatter_adapter = lambda kws: (None, kws) # pragma: no cover

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
