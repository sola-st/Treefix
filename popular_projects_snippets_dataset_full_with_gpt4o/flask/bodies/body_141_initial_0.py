from inspect import iscoroutinefunction # pragma: no cover

func = lambda: 'dummy function' # pragma: no cover
self = type('Mock', (object,), {'async_to_sync': lambda self, func: 'Mocked async_to_sync'})() # pragma: no cover

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
    _l_(19375)

    aux = self.async_to_sync(func)
    _l_(19374)
    exit(aux)
aux = func
_l_(19376)

exit(aux)
