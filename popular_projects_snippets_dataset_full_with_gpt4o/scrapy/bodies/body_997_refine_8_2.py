from twisted.internet import defer # pragma: no cover
from typing import Union # pragma: no cover
import logging # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
request = type('Mock', (object,), {'url': 'http://example.com'})() # pragma: no cover
spider = type('Mock', (object,), {'name': 'example_spider'})() # pragma: no cover
Response = type('Response', (object,), {'request': None}) # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws[0]) # pragma: no cover
signals = type('Mock', (object,), {})() # pragma: no cover
self.slot = type('Mock', (object,), {'add_request': lambda self, req: None, 'nextcall': type('Mock', (object,), {'schedule': lambda self: None})()})() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = type('Mock', (object,), {'crawled': lambda self, req, res, sp: ('message',)})() # pragma: no cover
logger.log = lambda level, msg, *args, **kwargs: print(f'{level}: {msg}') # pragma: no cover
self.signals = type('Mock', (object,), {'send_catch_log': lambda self, **kwargs: None})() # pragma: no cover
signals.response_received = 'response_received' # pragma: no cover
self.downloader = type('Mock', (object,), {'fetch': lambda self, req, sp: defer.Deferred()})() # pragma: no cover

from twisted.internet import defer # pragma: no cover
from typing import Union # pragma: no cover
import logging # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
request = type('Mock', (object,), {'url': 'http://example.com'})() # pragma: no cover
spider = type('Mock', (object,), {'name': 'example_spider'})() # pragma: no cover
Response = type('Response', (object,), {'request': None}) # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws[0]) # pragma: no cover
signals = type('Mock', (object,), {})() # pragma: no cover
self.slot = type('Mock', (object,), {'add_request': lambda req: None, 'nextcall': type('Mock', (object,), {'schedule': lambda: None})()})() # pragma: no cover
self.spider = spider # pragma: no cover
self.logformatter = type('Mock', (object,), {'crawled': lambda req, res, sp: ('message',)})() # pragma: no cover
logger.log = lambda level, msg, *args, **kwargs: print(f'{level}: {msg}') # pragma: no cover
self.signals = type('Mock', (object,), {'send_catch_log': lambda **kwargs: None})() # pragma: no cover
signals.response_received = 'response_received' # pragma: no cover
deferred_result = defer.Deferred() # pragma: no cover
deferred_result.addCallbacks = lambda callback, errback=None: None # pragma: no cover
deferred_result.addBoth = lambda callback: None # pragma: no cover
self.downloader = type('Mock', (object,), {'fetch': lambda req, sp: deferred_result})() # pragma: no cover

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
