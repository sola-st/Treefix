from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover
import logging # pragma: no cover

spider = 'my_spider' # pragma: no cover
logformatter_adapter = lambda logkws: (logkws['msg'], logkws['url'], logkws['response_status']) # pragma: no cover
signals = type('Signals', (object,), {'response_received': 'response_received_signal', 'send_catch_log': lambda self, signal, response, request, spider: None})() # pragma: no cover

from scrapy.http import Response, Request # pragma: no cover
import logging # pragma: no cover
from scrapy import signals # pragma: no cover

result = Response(url='http://example.com', status=200, body=b'Example body', request=Request(url='http://example.com')) # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
self = type('MockSelf', (object,), {'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda self, req, res, spider: {'url': req.url, 'status': res.status}})(), 'signals': type('MockSignals', (object,), {'send_catch_log': lambda self, signal, response, request, spider: None})()})() # pragma: no cover
spider = 'example_spider' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logger.log = lambda level, msg, *args, **kwargs: print(f'[{level}]: {msg}') # pragma: no cover
logformatter_adapter = lambda kws: (kws['url'], kws['status']) # pragma: no cover
signals = signals # pragma: no cover

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
