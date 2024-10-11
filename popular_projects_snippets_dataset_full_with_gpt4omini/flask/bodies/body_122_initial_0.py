from jinja2 import Environment # pragma: no cover

self = type('Mock', (object,), {'jinja_env': Environment()})() # pragma: no cover
name = 'custom_test' # pragma: no cover
f = lambda x: x * 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Register a custom template test.  Works exactly like the
        :meth:`template_test` decorator.

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """
self.jinja_env.tests[name or f.__name__] = f
_l_(8636)
