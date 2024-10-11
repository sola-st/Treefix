import logging # pragma: no cover
from unittest.mock import Mock # pragma: no cover

app = Mock() # pragma: no cover
app.name = 'my_flask_app' # pragma: no cover
app.debug = True # pragma: no cover
def has_level_handler(logger): return False # pragma: no cover
default_handler = logging.StreamHandler() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/logging.py
from l3.Runtime import _l_
"""Get the Flask app's logger and configure it if needed.

    The logger name will be the same as
    :attr:`app.import_name <flask.Flask.name>`.

    When :attr:`~flask.Flask.debug` is enabled, set the logger level to
    :data:`logging.DEBUG` if it is not set.

    If there is no handler for the logger's effective level, add a
    :class:`~logging.StreamHandler` for
    :func:`~flask.logging.wsgi_errors_stream` with a basic format.
    """
logger = logging.getLogger(app.name)
_l_(6598)

if app.debug and not logger.level:
    _l_(6600)

    logger.setLevel(logging.DEBUG)
    _l_(6599)

if not has_level_handler(logger):
    _l_(6602)

    logger.addHandler(default_handler)
    _l_(6601)
aux = logger
_l_(6603)

exit(aux)
