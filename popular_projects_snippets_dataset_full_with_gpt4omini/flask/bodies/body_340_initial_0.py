from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._get_exc_class_and_code = lambda x: (Exception, 400) # pragma: no cover
self.error_handler_spec = defaultdict(lambda: defaultdict(lambda: defaultdict(dict))) # pragma: no cover
code_or_exception = 'SomeError' # pragma: no cover
f = lambda: 'error handler function' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Alternative error attach function to the :meth:`errorhandler`
        decorator that is more straightforward to use for non decorator
        usage.

        .. versionadded:: 0.7
        """
exc_class, code = self._get_exc_class_and_code(code_or_exception)
_l_(4571)
self.error_handler_spec[None][code][exc_class] = f
_l_(4572)
