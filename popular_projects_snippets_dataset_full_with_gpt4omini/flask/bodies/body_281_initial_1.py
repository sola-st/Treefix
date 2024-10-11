import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

request = Mock(environ={'wsgi.errors': sys.stderr}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/logging.py
from l3.Runtime import _l_
"""Find the most appropriate error stream for the application. If a request
    is active, log to ``wsgi.errors``, otherwise use ``sys.stderr``.

    If you configure your own :class:`logging.StreamHandler`, you may want to
    use this for the stream. If you are using file or dict configuration and
    can't import this directly, you can refer to it as
    ``ext://flask.logging.wsgi_errors_stream``.
    """
aux = request.environ["wsgi.errors"] if request else sys.stderr
_l_(5076)
exit(aux)
