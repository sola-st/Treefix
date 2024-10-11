from jinja2 import BaseLoader # pragma: no cover

class DispatchingJinjaLoader(BaseLoader): # pragma: no cover
    def __init__(self, env): # pragma: no cover
        self.env = env # pragma: no cover
 # pragma: no cover
self = type('MockEnv', (), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Creates the loader for the Jinja2 environment.  Can be used to
        override just the loader and keeping the rest unchanged.  It's
        discouraged to override this function.  Instead one should override
        the :meth:`jinja_loader` function instead.

        The global loader dispatches between the loaders of the application
        and the individual blueprints.

        .. versionadded:: 0.7
        """
aux = DispatchingJinjaLoader(self)
_l_(4819)
exit(aux)
