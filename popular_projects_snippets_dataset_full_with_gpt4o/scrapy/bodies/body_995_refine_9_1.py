from unittest.mock import Mock, MagicMock # pragma: no cover
import logging # pragma: no cover
class Response: # pragma: no cover
    def __init__(self, request=None): # pragma: no cover
        self.request = request # pragma: no cover
class Request: # pragma: no cover
    pass # pragma: no cover

result = Mock(spec=Response) # pragma: no cover
request = Mock(spec=Request) # pragma: no cover
result.request = None # pragma: no cover
self = Mock() # pragma: no cover
self.logformatter = MagicMock() # pragma: no cover
spider = Mock() # pragma: no cover
logger = logging.getLogger() # pragma: no cover
logger.log = MagicMock() # pragma: no cover
logformatter_adapter = Mock(return_value=(logging.INFO, 'info message')) # pragma: no cover
signals = Mock() # pragma: no cover
self.signals = Mock() # pragma: no cover
self.signals.send_catch_log = MagicMock() # pragma: no cover
signals.response_received = Mock() # pragma: no cover

import logging # pragma: no cover
from scrapy.http import Response, Request # pragma: no cover
from scrapy import signals # pragma: no cover

result = Response('http://example.com') # pragma: no cover
request = Request('http://example.com') # pragma: no cover
self = type('Mock', (object,), {'logformatter': type('MockLogFormatter', (object,), {'crawled': lambda req, res, spi: {'message': 'Crawled successfully'}})(), 'signals': type('MockSignals', (object,), {'send_catch_log': lambda signal, response, request, spider: None})()})() # pragma: no cover
spider = object() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws.get('message', 'No message')) # pragma: no cover
signals = type('MockSignalsModule', (object,), {'response_received': 'response_received'})() # pragma: no cover

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
