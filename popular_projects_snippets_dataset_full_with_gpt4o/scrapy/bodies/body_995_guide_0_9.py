import logging # pragma: no cover
from types import SimpleNamespace # pragma: no cover

result = type('Response', (object,), {'request': None})() # pragma: no cover
request = type('Request', (object,), {})() # pragma: no cover
spider = type('Spider', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), {'logformatter': type('LogFormatter', (object,), {'crawled': lambda self, req, res, sp: None})(), 'signals': type('MockSignals', (object,), {'send_catch_log': lambda self, signal, response, request, spider: None })() })() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, 'Test log message') if logkws is not None else (logging.INFO, 'No log message') # pragma: no cover
signals = SimpleNamespace(response_received='response_received') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
if not isinstance(result, (Response, Request)):
    _l_(15579)

    raise TypeError(f"Incorrect type: expected Response or Request, got {type(result)}: {result!r}")
    _l_(15578)
if isinstance(result, Response):
    _l_(15586)

    if result.request is None:
        _l_(15581)

        result.request = request
        _l_(15580)
    logkws = self.logformatter.crawled(result.request, result, spider)
    _l_(15582)
    if logkws is not None:
        _l_(15584)

        logger.log(*logformatter_adapter(logkws), extra={"spider": spider})
        _l_(15583)
    self.signals.send_catch_log(
        signal=signals.response_received,
        response=result,
        request=result.request,
        spider=spider,
    )
    _l_(15585)
aux = result
_l_(15587)
exit(aux)
