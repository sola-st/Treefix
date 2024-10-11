import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {'logger': logging.getLogger()})() # pragma: no cover
request = type('Mock', (object,), {'path': '/example', 'method': 'GET'})() # pragma: no cover
exc_info = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Logs an exception.  This is called by :meth:`handle_exception`
        if debugging is disabled and right before the handler is called.
        The default implementation logs the exception as error on the
        :attr:`logger`.

        .. versionadded:: 0.8
        """
self.logger.error(
    f"Exception on {request.path} [{request.method}]", exc_info=exc_info
)
_l_(7067)
