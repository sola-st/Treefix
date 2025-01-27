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
_l_(22708)

if app.debug and not logger.level:
    _l_(22710)

    logger.setLevel(logging.DEBUG)
    _l_(22709)

if not has_level_handler(logger):
    _l_(22712)

    logger.addHandler(default_handler)
    _l_(22711)
aux = logger
_l_(22713)

exit(aux)
