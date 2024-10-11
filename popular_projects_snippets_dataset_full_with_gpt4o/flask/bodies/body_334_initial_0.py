self = type('Mock', (object,), {'teardown_request_funcs': {}})() # pragma: no cover
f = lambda: print('Function f called') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Register a function to be called when the request context is
        popped. Typically this happens at the end of each request, but
        contexts may be pushed manually as well during testing.

        .. code-block:: python

            with app.test_request_context():
                ...

        When the ``with`` block exits (or ``ctx.pop()`` is called), the
        teardown functions are called just before the request context is
        made inactive.

        When a teardown function was called because of an unhandled
        exception it will be passed an error object. If an
        :meth:`errorhandler` is registered, it will handle the exception
        and the teardown will not receive it.

        Teardown functions must avoid raising exceptions. If they
        execute code that might fail they must surround that code with a
        ``try``/``except`` block and log any errors.

        The return values of teardown functions are ignored.
        """
self.teardown_request_funcs.setdefault(None, []).append(f)
_l_(22667)
aux = f
_l_(22668)
exit(aux)
