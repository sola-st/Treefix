from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover
import logging # pragma: no cover

result = Response(url='http://example.com', body=b'Example response') # pragma: no cover
Request = type('MockRequest', (object,), {'url': 'http://example.com', 'method': 'GET'}) # pragma: no cover
request = Request() # pragma: no cover
self = type('MockSelf', (object,), {'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda self, req, res, sp: {'url': req.url, 'status': res.status, 'spider': sp}})(), 'signals': type('MockSignals', (object,), {})()})() # pragma: no cover
spider = 'example_spider' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logger.log = lambda level, msg, extra: print(f'[{level}] {msg}', extra) # pragma: no cover
logformatter_adapter = lambda kws: (kws['url'], kws['status']) # pragma: no cover
signals.response_received = 'response_received' # pragma: no cover

from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover
import logging # pragma: no cover

result = Response(url='http://example.com', status=200, body=b'Example response') # pragma: no cover
Request = type('MockRequest', (object,), {'url': 'http://example.com', 'method': 'GET'}) # pragma: no cover
request = Request() # pragma: no cover
self = type('MockSelf', (object,), {'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda self, req, res, sp: {'url': req.url, 'status': res.status, 'spider': sp}})(), 'signals': type('MockSignals', (object,), {'send_catch_log': lambda self, signal, response, request, spider: print(f'Signal triggered: {signal}, Response: {response}, Request URL: {request.url}, Spider: {spider}')})()})() # pragma: no cover
spider = 'test_spider' # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logger.log = lambda level, msg, extra=None: print(f'[{level}] {msg}, Extra: {extra}') # pragma: no cover
signals.response_received = 'response_received_signal' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
if not isinstance(result, (Response, Request)):
    _l_(4055)

    raise TypeError(f"Incorrect type: expected Response or Request, got {type(result)}: {result!r}")
    _l_(4054)
if isinstance(result, Response):
    _l_(4062)

    if result.request is None:
        _l_(4057)

        result.request = request
        _l_(4056)
    logkws = self.logformatter.crawled(result.request, result, spider)
    _l_(4058)
    if logkws is not None:
        _l_(4060)

        logger.log(*logformatter_adapter(logkws), extra={"spider": spider})
        _l_(4059)
    self.signals.send_catch_log(
        signal=signals.response_received,
        response=result,
        request=result.request,
        spider=spider,
    )
    _l_(4061)
aux = result
_l_(4063)
exit(aux)
