from unittest.mock import Mock, MagicMock # pragma: no cover
import logging # pragma: no cover

result = Mock(spec=['request']) # pragma: no cover
Response = Mock() # pragma: no cover
Request = Mock() # pragma: no cover
request = Mock() # pragma: no cover
self = Mock(LogFormatter=Mock(), signals=Mock()) # pragma: no cover
spider = Mock() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logformatter_adapter = Mock(return_value=(logging.INFO, 'Formatted log message')) # pragma: no cover
signals = Mock(response_received='response_received') # pragma: no cover
result.request = None # pragma: no cover
self.logformatter = Mock(crawled=Mock(return_value={'msg': 'log message'})) # pragma: no cover
logger.log = Mock() # pragma: no cover
self.signals.send_catch_log = Mock() # pragma: no cover

from scrapy.http import Response, Request # pragma: no cover
import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

result = Response(url='http://example.com') # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
self = type('Mock', (object,), {'logformatter': Mock(), 'signals': Mock()})() # pragma: no cover
spider = Mock() # pragma: no cover
logger = logging.getLogger(__name__) # pragma: no cover
logformatter_adapter = lambda logkws: (logging.INFO, logkws.get('message', 'No message')) # pragma: no cover
signals = type('MockSignals', (object,), {'response_received': Mock()})() # pragma: no cover
self.logformatter.crawled = lambda req, res, spider: {'message': 'Crawled successfully'} # pragma: no cover
self.signals.send_catch_log = lambda signal, response, request, spider: None # pragma: no cover
logger.log = lambda level, msg, extra: None # pragma: no cover

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
