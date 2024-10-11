import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

dont_log = None # pragma: no cover
failure = Mock() # pragma: no cover
failure.value = 'error_value' # pragma: no cover
logger = Mock() # pragma: no cover
recv = 'signal_receiver' # pragma: no cover
def failure_to_exc_info(failure): return ('type', 'value', 'traceback') # pragma: no cover
spider = 'spider_instance' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/signal.py
from l3.Runtime import _l_
if dont_log is None or not isinstance(failure.value, dont_log):
    _l_(8217)

    logger.error("Error caught on signal handler: %(receiver)s",
                 {'receiver': recv},
                 exc_info=failure_to_exc_info(failure),
                 extra={'spider': spider})
    _l_(8216)
aux = failure
_l_(8218)
exit(aux)
