import typing as t # pragma: no cover

exc_class_or_code = 404 # pragma: no cover
HTTPException = type('HTTPException', (Exception,), {'code': None}) # pragma: no cover

import typing as t # pragma: no cover

exc_class_or_code = 404 # pragma: no cover
default_exceptions = {404: type('NotFound', (Exception,), {'code': 404})} # pragma: no cover
HTTPException = type('HTTPException', (Exception,), {'code': None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Get the exception class being handled. For HTTP status codes
        or ``HTTPException`` subclasses, return both the exception and
        status code.

        :param exc_class_or_code: Any exception class, or an HTTP status
            code as an integer.
        """
exc_class: t.Type[Exception]
_l_(20769)

if isinstance(exc_class_or_code, int):
    _l_(20775)

    try:
        _l_(20773)

        exc_class = default_exceptions[exc_class_or_code]
        _l_(20770)
    except KeyError:
        _l_(20772)

        raise ValueError(
            f"'{exc_class_or_code}' is not a recognized HTTP"
            " error code. Use a subclass of HTTPException with"
            " that code instead."
        ) from None
        _l_(20771)
else:
    exc_class = exc_class_or_code
    _l_(20774)

if isinstance(exc_class, Exception):
    _l_(20777)

    raise TypeError(
        f"{exc_class!r} is an instance, not a class. Handlers"
        " can only be registered for Exception classes or HTTP"
        " error codes."
    )
    _l_(20776)

if not issubclass(exc_class, Exception):
    _l_(20779)

    raise ValueError(
        f"'{exc_class.__name__}' is not a subclass of Exception."
        " Handlers can only be registered for Exception classes"
        " or HTTP error codes."
    )
    _l_(20778)

if issubclass(exc_class, HTTPException):
    _l_(20782)

    aux = (exc_class, exc_class.code)
    _l_(20780)
    exit(aux)
else:
    aux = (exc_class, None)
    _l_(20781)
    exit(aux)
