import logging # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover

result = Response(url='http://example.com') # pragma: no cover
Response = type('Response', (object,), {'request': None}) # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
request = Request() # pragma: no cover
spider = type('Spider', (object,), {})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = lambda logkws: ('INFO', logkws.get('message', 'No message')) # pragma: no cover
logformatter = type('LogFormatter', (object,), {'crawled': lambda *args: {'message': 'Crawled'}})() # pragma: no cover
self = type('Mock', (object,), {'logformatter': logformatter, 'signals': type('Signals', (object,), {'send_catch_log': lambda *args, **kwargs: None})()})() # pragma: no cover

import logging # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
from scrapy.signalmanager import SignalManager # pragma: no cover
from scrapy import signals # pragma: no cover

result = Response('http://example.com') # pragma: no cover
request = Request('http://example.com') # pragma: no cover
logger = logging.getLogger(__name__) # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws.get('msg', '')) # pragma: no cover
signals.response_received = 'response_received' # pragma: no cover

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
