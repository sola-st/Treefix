import sys # pragma: no cover

sys.modules.pop('logging', None) # pragma: no cover
logging = type('Mock', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5191830/how-do-i-log-a-python-error-with-debug-information
from l3.Runtime import _l_
try:
    import logging
    _l_(14223)

except ImportError:
    pass
try:
    from contextlib import AbstractContextManager
    _l_(14225)

except ImportError:
    pass


class LogError(AbstractContextManager):
    _l_(14231)


    def __init__(self, logger=None):
        _l_(14227)

        self.logger = logger.name if isinstance(logger, logging.Logger) else logger
        _l_(14226)

    def __exit__(self, exc_type, exc_value, traceback):
        _l_(14230)

        if exc_value is not None:
            _l_(14229)

            logging.getLogger(self.logger).exception(exc_value)
            _l_(14228)


with LogError():
    _l_(14233)

    1/0
    _l_(14232)

