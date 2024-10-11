from flask import stream_with_context, request, Response # pragma: no cover
import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

generator_or_function = lambda *args, **kwargs: (yield 'Generated value') # pragma: no cover
_cv_request = type('MockRequestContext', (object,), {'get': staticmethod(lambda _: 'MockContext')})() # pragma: no cover

from flask import stream_with_context, request, Response # pragma: no cover
import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

def generator_or_function(): yield 'Generated value' # pragma: no cover
_cv_request = type('MockRequestContext', (object,), {'get': staticmethod(lambda _: 'MockContext')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Request contexts disappear when the response is started on the server.
    This is done for efficiency reasons and to make it less likely to encounter
    memory leaks with badly written WSGI middlewares.  The downside is that if
    you are using streamed responses, the generator cannot access request bound
    information any more.

    This function however can help you keep the context around for longer::

        from flask import stream_with_context, request, Response

        @app.route('/stream')
        def streamed_response():
            @stream_with_context
            def generate():
                yield 'Hello '
                yield request.args['name']
                yield '!'
            return Response(generate())

    Alternatively it can also be used around a specific generator::

        from flask import stream_with_context, request, Response

        @app.route('/stream')
        def streamed_response():
            def generate():
                yield 'Hello '
                yield request.args['name']
                yield '!'
            return Response(stream_with_context(generate()))

    .. versionadded:: 0.9
    """
try:
    _l_(5296)

    gen = iter(generator_or_function)  # type: ignore
    _l_(5290)  # type: ignore
except TypeError:
    _l_(5295)


    def decorator(*args: t.Any, **kwargs: t.Any) -> t.Any:
        _l_(5293)

        gen = generator_or_function(*args, **kwargs)  # type: ignore
        _l_(5291)  # type: ignore
        aux = stream_with_context(gen)
        _l_(5292)
        exit(aux)
    aux = update_wrapper(decorator, generator_or_function)  # type: ignore
    _l_(5294)  # type: ignore

    exit(aux)  # type: ignore

def generator() -> t.Generator:
    _l_(5307)

    ctx = _cv_request.get(None)
    _l_(5297)
    if ctx is None:
        _l_(5299)

        raise RuntimeError(
            "'stream_with_context' can only be used when a request"
            " context is active, such as in a view function."
        )
        _l_(5298)
    with ctx:
        _l_(5306)

        aux = None
        _l_(5300)
        # Dummy sentinel.  Has to be inside the context block or we're
        # not actually keeping the context around.
        exit(aux)

        # The try/finally is here so that if someone passes a WSGI level
        # iterator in we're still running the cleanup logic.  Generators
        # don't need that because they are closed on their destruction
        # automatically.
        try:
            _l_(5305)

            aux = gen
            _l_(5301)
            exit(aux)
        finally:
            _l_(5304)

            if hasattr(gen, "close"):
                _l_(5303)

                gen.close()
                _l_(5302)
wrapped_g = generator()
_l_(5308)
next(wrapped_g)
_l_(5309)
aux = wrapped_g
_l_(5310)
exit(aux)
