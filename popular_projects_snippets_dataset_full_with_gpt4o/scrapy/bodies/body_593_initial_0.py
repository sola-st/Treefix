import logging # pragma: no cover
from types import SimpleNamespace # pragma: no cover

dont_log = type('MockDontLog', (object,), {}) # pragma: no cover
failure = SimpleNamespace(value=type('MockFailureValue', (object,), {})) # pragma: no cover
logger = logging.getLogger('mockLogger') # pragma: no cover
recv = 'mockReceiver' # pragma: no cover
failure_to_exc_info = lambda failure: (None, None, None) # pragma: no cover
spider = 'mockSpider' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/signal.py
from l3.Runtime import _l_
if dont_log is None or not isinstance(failure.value, dont_log):
    _l_(19421)

    logger.error("Error caught on signal handler: %(receiver)s",
                 {'receiver': recv},
                 exc_info=failure_to_exc_info(failure),
                 extra={'spider': spider})
    _l_(19420)
aux = failure
_l_(19422)
exit(aux)
