from flask import Flask, current_app # pragma: no cover
from werkzeug.exceptions import abort # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
code = 404 # pragma: no cover
args = ('Not Found',) # pragma: no cover
kwargs = {'extra_info': 'Resource does not exist'} # pragma: no cover
_wz_abort = abort # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Raise an :exc:`~werkzeug.exceptions.HTTPException` for the given
    status code.

    If :data:`~flask.current_app` is available, it will call its
    :attr:`~flask.Flask.aborter` object, otherwise it will use
    :func:`werkzeug.exceptions.abort`.

    :param code: The status code for the exception, which must be
        registered in ``app.aborter``.
    :param args: Passed to the exception.
    :param kwargs: Passed to the exception.

    .. versionadded:: 2.2
        Calls ``current_app.aborter`` if available instead of always
        using Werkzeug's default ``abort``.
    """
if current_app:
    _l_(4581)

    current_app.aborter(code, *args, **kwargs)
    _l_(4580)

_wz_abort(code, *args, **kwargs)
_l_(4582)
