from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover

request = Request(url='http://example.com') # pragma: no cover
result = Response(url='http://example.com', status=200, request=request) # pragma: no cover
logger = type('MockLogger', (), {'log': lambda self, level, msg, extra: print(level, msg, extra)})() # pragma: no cover
spider = 'mock_spider' # pragma: no cover
self = type('MockSelf', (), {'logformatter': type('MockLogFormatter', (), {'crawled': lambda self, req, res, spider: {'url': req.url, 'status': res.status}})(), 'signals': signals})() # pragma: no cover

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
