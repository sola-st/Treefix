from asyncio import iscoroutinefunction # pragma: no cover
from types import FunctionType # pragma: no cover

func = lambda: 'I am a regular function' # pragma: no cover
self = type('Mock', (object,), {'async_to_sync': lambda self, f: f()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Ensure that the function is synchronous for WSGI workers.
        Plain ``def`` functions are returned as-is. ``async def``
        functions are wrapped to run and wait for the response.

        Override this method to change how the app runs async views.

        .. versionadded:: 2.0
        """
if iscoroutinefunction(func):
    _l_(8242)

    aux = self.async_to_sync(func)
    _l_(8241)
    exit(aux)
aux = func
_l_(8243)

exit(aux)
