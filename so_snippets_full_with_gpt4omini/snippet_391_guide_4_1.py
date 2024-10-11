import logging # pragma: no cover
from contextlib import AbstractContextManager # pragma: no cover

logger = logging.getLogger('test_logger') # pragma: no cover
logging.basicConfig(level=logging.DEBUG) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5191830/how-do-i-log-a-python-error-with-debug-information
from l3.Runtime import _l_
try:
    import logging
    _l_(1804)

except ImportError:
    pass
try:
    from contextlib import AbstractContextManager
    _l_(1806)

except ImportError:
    pass


class LogError(AbstractContextManager):
    _l_(1812)


    def __init__(self, logger=None):
        _l_(1808)

        self.logger = logger.name if isinstance(logger, logging.Logger) else logger
        _l_(1807)

    def __exit__(self, exc_type, exc_value, traceback):
        _l_(1811)

        if exc_value is not None:
            _l_(1810)

            logging.getLogger(self.logger).exception(exc_value)
            _l_(1809)


with LogError():
    _l_(1814)

    1/0
    _l_(1813)

