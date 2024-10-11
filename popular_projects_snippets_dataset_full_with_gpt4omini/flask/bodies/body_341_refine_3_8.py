exc_class_or_code = 404 # pragma: no cover
class HTTPException(Exception): # pragma: no cover
    code = 404 # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover

from typing import Type, Dict, Any # pragma: no cover
class HTTPException(Exception): # pragma: no cover
    def __init__(self, code: int): # pragma: no cover
        self.code = code # pragma: no cover

exc_class_or_code = 404 # pragma: no cover
default_exceptions: Dict[int, Type[Exception]] = { # pragma: no cover
    404: HTTPException(404), # pragma: no cover
    500: HTTPException(500) # pragma: no cover
} # pragma: no cover
HTTPException = type('HTTPException', (Exception,), {'code': 200}) # pragma: no cover
t = type # pragma: no cover

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
_l_(9557)

if isinstance(exc_class_or_code, int):
    _l_(9563)

    try:
        _l_(9561)

        exc_class = default_exceptions[exc_class_or_code]
        _l_(9558)
    except KeyError:
        _l_(9560)

        raise ValueError(
            f"'{exc_class_or_code}' is not a recognized HTTP"
            " error code. Use a subclass of HTTPException with"
            " that code instead."
        ) from None
        _l_(9559)
else:
    exc_class = exc_class_or_code
    _l_(9562)

if isinstance(exc_class, Exception):
    _l_(9565)

    raise TypeError(
        f"{exc_class!r} is an instance, not a class. Handlers"
        " can only be registered for Exception classes or HTTP"
        " error codes."
    )
    _l_(9564)

if not issubclass(exc_class, Exception):
    _l_(9567)

    raise ValueError(
        f"'{exc_class.__name__}' is not a subclass of Exception."
        " Handlers can only be registered for Exception classes"
        " or HTTP error codes."
    )
    _l_(9566)

if issubclass(exc_class, HTTPException):
    _l_(9570)

    aux = (exc_class, exc_class.code)
    _l_(9568)
    exit(aux)
else:
    aux = (exc_class, None)
    _l_(9569)
    exit(aux)
