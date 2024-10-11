import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

Response = type('Response', (object,), {'request': None}) # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
result = Response() # pragma: no cover
request = Request() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
logger.setLevel(logging.DEBUG) # pragma: no cover
logger.addHandler(logging.StreamHandler()) # pragma: no cover
logformatter_adapter = lambda logkws: (logkws['level'], logkws['msg']) # pragma: no cover
self = type('Self', (object,), {'logformatter': Mock(), 'signals': Mock()})() # pragma: no cover
self.logformatter.crawled = Mock(return_value={'level': logging.INFO, 'msg': 'Crawled log'}) # pragma: no cover
self.signals.send_catch_log = Mock() # pragma: no cover
signals = type('Signals', (object,), {'response_received': 'response_received'})() # pragma: no cover
spider = Mock() # pragma: no cover

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
