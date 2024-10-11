from jinja2 import Environment, FileSystemLoader # pragma: no cover
from werkzeug.utils import import_string # pragma: no cover

class DispatchingJinjaLoader:# pragma: no cover
    def __init__(self, app_or_blueprint):# pragma: no cover
        self.app_or_blueprint = app_or_blueprint # pragma: no cover
self = type('MockApp', (object,), {})() # pragma: no cover

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
_l_(22543)
exit(aux)
